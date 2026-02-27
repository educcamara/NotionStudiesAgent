from google.adk.agents.llm_agent import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.adk.plugins import LoggingPlugin
from google.adk.tools import AgentTool

from notion_studies.agents.recipe_checker import recipe_checker
from notion_studies.agents.sequential_agent import sequential_agent
from notion_studies.util.retry_config import retry_config

root_agent = Agent(
    name='root_agent',
    model=Gemini(
        model='gemini-2.5-pro',
        retry_options=retry_config
    ),
    description='Notion Recipe Agent — checks Notion for a recipe and creates it if missing.',
    instruction="""
You are a recipe assistant that manages a Notion recipe database located at Personal Home/Recipes.

When the user requests a recipe, follow these steps strictly:

1. Use the `recipe_checker` tool to search for the recipe in Personal Home/Recipes.
2. Evaluate the result:
   - If "status": "found" → return the recipe content to the user directly. Do NOT run the creation pipeline.
   - If "status": "not found" → call the `sequential_agent` tool passing the following message:
     "The recipe '<recipe_name>' was not found in Notion. Please research it online and create it."
   - If "status": "error" → inform the user that the lookup failed and suggest they try again.

Rules:
- Never skip the check step.
- Never create a recipe that already exists.
- Do not invent or hallucinate recipe content.
- Keep your final response concise and user-friendly.
""",
    tools=[
        AgentTool(recipe_checker),
        AgentTool(sequential_agent),
    ]
)


app = App(
    name="notion_studies",
    root_agent=root_agent,
    plugins=[
        LoggingPlugin()
    ]
)