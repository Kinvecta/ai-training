// ticket-desk: a minimal MCP server (TypeScript SDK v2)
import {
    acceptedContent,
    inputRequired,
    inputResponse,
    McpServer,
    ResourceTemplate
} from '@modelcontextprotocol/server';
import type { CallToolResult, InputRequiredResult } from '@modelcontextprotocol/server';
import * as z from 'zod/v4';

// Stand-in for a real ticketing API
const TICKETS: Record<string, { id: string; title: string; status: 'open' | 'closed'; priority: string }> = {
    'TCK-1001': { id: 'TCK-1001', title: 'VPN drops every 30 min', status: 'open', priority: 'high' },
    'TCK-1002': { id: 'TCK-1002', title: 'Printer on 3rd floor offline', status: 'open', priority: 'low' }
};

const TicketId = z.string().regex(/^TCK-\d{4}$/).describe('Ticket ID, e.g. TCK-1001');
const Confirm = z.object({ confirm: z.boolean().meta({ title: 'Yes, close this ticket' }) });

// Factory: the SDK calls this whenever it needs a fresh server instance
export function createServer(): McpServer {
    const server = new McpServer({ name: 'ticket-desk', version: '1.0.0' });

    // 1) Read-only tool with structured output
    server.registerTool(
        'get_ticket',
        {
            title: 'Look up a ticket',
            description: 'Return one help-desk ticket by ID. Read-only.',
            inputSchema: z.object({ ticket_id: TicketId }),
            outputSchema: z.object({ id: z.string(), title: z.string(), status: z.enum(['open', 'closed']), priority: z.string() }),
            annotations: { readOnlyHint: true, openWorldHint: false }
        },
        async ({ ticket_id }) => {
            console.error(`get_ticket ${ticket_id}`); // stderr only
            const t = TICKETS[ticket_id];
            if (!t) return { content: [{ type: 'text', text: `No ticket ${ticket_id}.` }], isError: true };
            return { content: [{ type: 'text', text: JSON.stringify(t) }], structuredContent: t };
        }
    );

    // 2) Action tool that requires human confirmation (MRTR input_required)
    server.registerTool(
        'close_ticket',
        {
            title: 'Close a ticket',
            description: 'Close a ticket with a resolution note. Asks the user to confirm first.',
            inputSchema: z.object({ ticket_id: TicketId, resolution: z.string().min(5).max(500) }),
            annotations: { readOnlyHint: false, destructiveHint: false, idempotentHint: true, openWorldHint: false }
        },
        async ({ ticket_id, resolution }, ctx): Promise<CallToolResult | InputRequiredResult> => {
            if (!TICKETS[ticket_id]) return { content: [{ type: 'text', text: `No ticket ${ticket_id}.` }], isError: true };
            // A decline/cancel must end the call, or the client is asked again
            const view = inputResponse(ctx.mcpReq.inputResponses, 'confirm');
            if (view.kind === 'elicit' && view.action !== 'accept') {
                return { content: [{ type: 'text', text: `${ticket_id} NOT closed (user chose ${view.action}).` }] };
            }
            const answer = acceptedContent(ctx.mcpReq.inputResponses, 'confirm', Confirm);
            if (answer === undefined) {
                return inputRequired({
                    inputRequests: {
                        confirm: inputRequired.elicit({
                            message: `Close ticket ${ticket_id}? This notifies the requester.`,
                            requestedSchema: Confirm
                        })
                    }
                });
            }
            if (!answer.confirm) return { content: [{ type: 'text', text: `${ticket_id} NOT closed: user did not confirm.` }] };
            TICKETS[ticket_id].status = 'closed';
            console.error(`AUDIT close_ticket ${ticket_id} resolution=${JSON.stringify(resolution)}`);
            return { content: [{ type: 'text', text: `${ticket_id} closed.` }] };
        }
    );

    // 3) Resource template
    server.registerResource(
        'ticket',
        new ResourceTemplate('tickets://{ticketId}', { list: undefined }),
        { title: 'Ticket JSON', description: 'A ticket as JSON', mimeType: 'application/json' },
        async (uri, { ticketId }) => ({
            contents: [{ uri: uri.href, mimeType: 'application/json', text: JSON.stringify(TICKETS[String(ticketId)] ?? {}) }]
        })
    );

    // 4) Prompt
    server.registerPrompt(
        'triage_ticket',
        {
            title: 'Triage a ticket',
            description: 'Draft a triage plan for one ticket',
            argsSchema: z.object({ ticket_id: z.string() })
        },
        ({ ticket_id }) => ({
            messages: [
                {
                    role: 'user' as const,
                    content: { type: 'text' as const, text: `Use get_ticket to read ${ticket_id}. Propose priority, owner and next step. Do not close it.` }
                }
            ]
        })
    );

    return server;
}
