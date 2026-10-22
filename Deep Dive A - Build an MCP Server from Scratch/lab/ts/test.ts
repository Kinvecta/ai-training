import assert from 'node:assert/strict';
import { Client, StreamableHTTPClientTransport } from '@modelcontextprotocol/client';
import { createMcpHandler } from '@modelcontextprotocol/server';
import { createServer } from './server.js';

const handler = createMcpHandler(createServer);
const transport = new StreamableHTTPClientTransport(new URL('http://test.local/mcp'), {
    fetch: (url, init) => handler.fetch(new Request(url, init))
});
const client = new Client(
    { name: 'test', version: '1.0.0' },
    { versionNegotiation: { mode: 'auto' }, capabilities: { elicitation: { form: {} } } }
);
let answer: any = { action: 'decline' };
client.setRequestHandler('elicitation/create', async (req: any) => {
    console.log('ELICIT:', req.params.message);
    return answer;
});
await client.connect(transport);
console.log('era', client.getProtocolEra());

const tools = await client.listTools();
console.log(tools.tools.map(t => [t.name, t.annotations]));
const r1 = await client.callTool({ name: 'get_ticket', arguments: { ticket_id: 'TCK-1001' } });
console.log(r1.structuredContent);
const bad = await client.callTool({ name: 'get_ticket', arguments: { ticket_id: 'DROP TABLE' } });
console.log(bad.isError, (bad.content as any)[0].text);

const r2 = await client.callTool({ name: 'close_ticket', arguments: { ticket_id: 'TCK-1002', resolution: 'Replaced toner' } });
console.log((r2.content as any)[0].text);
answer = { action: 'accept', content: { confirm: true } };
const r3 = await client.callTool({ name: 'close_ticket', arguments: { ticket_id: 'TCK-1002', resolution: 'Replaced toner' } });
console.log((r3.content as any)[0].text);
assert.match((r3.content as any)[0].text, /closed\./);

const res = await client.readResource({ uri: 'tickets://TCK-1002' });
console.log(res.contents);
const p = await client.getPrompt({ name: 'triage_ticket', arguments: { ticket_id: 'TCK-1002' } });
console.log(p.messages[0]);
await client.close();
