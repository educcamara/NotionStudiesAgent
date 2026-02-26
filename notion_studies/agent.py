from google.adk.agents.llm_agent import Agent

from notion_studies.notion_tool import notion_tool

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Notion Agent',
    instruction='You are a Notion assistant that can answer questions about the user\'s Notion workspace. You have access to a tool that allows you to query the user\'s Notion workspace. Use this tool to find the information needed to answer user questions.',
    tools=[notion_tool]
)