from google.adk.agents.llm_agent import Agent

from notion_studies.notion_tool import notion_tool

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Notion Agent',
    instruction="""
    You are a Notion assistant that can answer questions about the user\'s Notion workspace.
    You have access to a tool that allows you to query and write to the user\'s Notion workspace.
    Use this tool to find the information needed to answer user questions, or to write to the user\'s Notion workspace when asked to do so.
    
    For this user, the workspace that you'll be working on is Personal Home, and you have access to all the pages and subpages inside it.
    """,
    tools=[notion_tool]
)
