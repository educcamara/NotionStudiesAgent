from google.adk import Agent
from google.adk.models import Gemini
from google.adk.tools import AgentTool

from notion_studies.agents.recipe_writer import recipe_writer
from notion_studies.util.retry_config import retry_config

aggregator_agent = Agent(
    name="aggregator_agent",
    model=Gemini(
        model='gemini-2.5-pro',
        retry_options=retry_config
    ),
    description="""
    Gets the results from recipe_researcher and recipe_file_creator, and aggregates them to provide a final status of the overall process.
    """,
    instruction="""
The previous steps have produced the following outputs:
- Recipe Researcher Output: {recipe_researcher}
- Recipe File Creator Output: {recipe_file_creator}

Your task is to:
1. Save the recipe content with the recipe_writer tool in the created Notion file if the recipe was not found and the file was created.
2. If it all went as expected, return:
{
    "status": "success",
    "notion_file_path": "<the path of the created recipe file in Notion>",
    "recipe_content": "<the recipe content that was saved in Notion>"
}

if there was an error in any of the previous steps, return:
{
    "status": "error",
    "description": "<brief description of what went wrong>"
}
    """,
    tools=[AgentTool(recipe_writer)]
)