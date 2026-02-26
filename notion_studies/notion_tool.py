import os
from dotenv import load_dotenv
from google.adk.tools.mcp_tool import McpToolset, StdioConnectionParams
from mcp import StdioServerParameters

load_dotenv()
if tok:=os.environ.get("NOTION_TOKEN"):
    NOTION_TOKEN: str = tok
else:
    raise ValueError("NOTION_TOKEN environment variable not set. Please set it in your .env file or environment variables.")

notion_tool = (
    McpToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command="npx",
                args=["-y", "@notionhq/notion-mcp-server"],
                env={"NOTION_TOKEN": NOTION_TOKEN},
            ),
            timeout=30,
        ),
    )
)
