import pytest
from mcp import Client

from server import mcp, TICKETS


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
async def client():
    async with Client(mcp, raise_exceptions=True) as c:
        yield c


@pytest.mark.anyio
async def test_lists_tools_with_annotations(client: Client):
    tools = {t.name: t for t in (await client.list_tools()).tools}
    assert set(tools) == {"get_ticket", "close_ticket"}
    assert tools["get_ticket"].annotations.read_only_hint is True
    assert tools["get_ticket"].output_schema is not None
    assert "confirm" not in tools["close_ticket"].input_schema["properties"]
    print(tools["get_ticket"].input_schema)
    print(tools["get_ticket"].output_schema)


@pytest.mark.anyio
async def test_get_ticket(client: Client):
    r = await client.call_tool("get_ticket", {"ticket_id": "TCK-1001"})
    assert r.structured_content["status"] == "open"
    print(r)


@pytest.mark.anyio
async def test_bad_id_is_tool_error(client: Client):
    r = await client.call_tool("get_ticket", {"ticket_id": "1001; DROP TABLE"})
    assert r.is_error
    print(r.content[0].text)
    r = await client.call_tool("get_ticket", {"ticket_id": "TCK-9999"})
    assert r.is_error
    print(r.content[0].text)


@pytest.mark.anyio
async def test_resource_and_prompt(client: Client):
    res = await client.read_resource("tickets://TCK-1002")
    assert "Printer" in res.contents[0].text
    p = await client.get_prompt("triage_ticket", {"ticket_id": "TCK-1002"})
    print(p.messages)


from mcp.types import ElicitResult


def make_cb(answer):
    async def cb(context, params):
        print("ELICIT:", params.message, params.requested_schema)
        return answer
    return cb


@pytest.mark.anyio
@pytest.mark.parametrize("mode", ["auto", "legacy"])
async def test_close_requires_confirmation(mode):
    TICKETS["TCK-1002"]["status"] = "open"
    async with Client(mcp, mode=mode, elicitation_callback=make_cb(ElicitResult(action="decline"))) as c:
        r = await c.call_tool("close_ticket", {"ticket_id": "TCK-1002", "resolution": "Replaced toner"})
        print(mode, r.content[0].text)
        assert TICKETS["TCK-1002"]["status"] == "open"
    async with Client(mcp, mode=mode, elicitation_callback=make_cb(ElicitResult(action="accept", content={"confirm": True}))) as c:
        r = await c.call_tool("close_ticket", {"ticket_id": "TCK-1002", "resolution": "Replaced toner"})
        print(mode, r.content[0].text)
        assert TICKETS["TCK-1002"]["status"] == "closed"
