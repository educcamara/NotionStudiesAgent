from google.adk.agents.llm_agent import Agent
from google.adk.models import Gemini
from google.adk.tools import AgentTool

from notion_studies.agents.sequential_agent import sequential_agent
from notion_studies.util.retry_config import retry_config

decision_agent = Agent(
    name='decision_agent',
    model=Gemini(
        model='gemini-2.5-pro',
        retry_options=retry_config
    ),
    description='Evaluates the recipe_checker result and decides whether to return the recipe or trigger the creation pipeline.',
    instruction="""
You are a recipe assistant that manages a Notion recipe database located at Personal Home/Recipes.

The recipe_checker has already run and produced this result:
{recipe_checker}

Based on this result:
- If "status": "found" → return the recipe content to the user directly. Do NOT run the creation pipeline.
- If "status": "not found" → call the `sequential_agent` tool passing the message:
  "The recipe '<recipe_name>' was not found in Notion. Please research it online and create it."
- If "status": "error" → inform the user that the lookup failed and suggest they try again.

Rules:
- Never create a recipe that already exists.
- Do not invent or hallucinate recipe content.
- Keep your final response concise and user-friendly.
""",
    tools=[
        AgentTool(sequential_agent),
    ]
)