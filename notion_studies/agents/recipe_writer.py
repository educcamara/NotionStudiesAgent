from google.adk.agents.llm_agent import Agent
from notion_studies.notion_tool import notion_tool


recipe_writer = Agent(
    model='gemini-2.5-pro',
    name='recipe_writer',
    description='Fills the existing recipe template in Notion at Personal Home/Recipes/<Recipe Name> with the provided recipe content.',
    instruction="""
You are a deterministic recipe writing agent.

Your task is to:
1. Receive a complete recipe.
2. Fill recipe page in Personal Home/Recipes/<Recipe Name> with the recipe content, matching this template structure:
    - Ingredients
    - Preparation
    - Observations

Operational Rules:
- Do not provide suggestions or explanations.
- DO NOT create a new "Recipes" page. It MUST already exist from the previous step. Your only task is to fill in the content in the existing template.

If the recipe is successfully written, return:
{
    "status": "written"
}

If there is an error, return:
{
    "status": "error"
}

Do not include any text outside the JSON response.
    """,
    tools=[notion_tool()],
    output_key='recipe_writer'
)