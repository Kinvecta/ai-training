import { createMcpExpressApp } from '@modelcontextprotocol/express';
import { toNodeHandler } from '@modelcontextprotocol/node';
import { createMcpHandler } from '@modelcontextprotocol/server';
import { createServer } from './server.js';

const handler = createMcpHandler(createServer); // fresh McpServer per request; stateless
const app = createMcpExpressApp();              // express.json() + Host/Origin checks on localhost
const node = toNodeHandler(handler);
app.all('/mcp', (req, res) => void node(req, res, req.body));
app.listen(3000, '127.0.0.1', () => console.error('ticket-desk on http://127.0.0.1:3000/mcp'));
