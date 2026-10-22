import { serveStdio } from '@modelcontextprotocol/server/stdio';
import { createServer } from './server.js';

void serveStdio(createServer);
console.error('ticket-desk MCP server running on stdio');
