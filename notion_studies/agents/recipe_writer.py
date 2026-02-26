from google.adk.agents.llm_agent import Agent
from notion_studies.notion_tool import notion_tool


recipe_writer = Agent(
    model='gemini-3-flash-preview',
    name='recipe_writer',
    description='Fills the existing recipe template in Notion at Personal Home/Recipes/<Recipe Name> with the provided recipe content.',
    instruction="""
You are a deterministic recipe writing agent.

Your task is to:
1. Receive a complete recipe.
2. Fill the existing template in Personal Home/Recipes/<Recipe Name> with the recipe content, matching the template structure (e.g., Ingredients, Preparation, Observations).

Operational Rules:
- Only fill the template with the recipe content.
- Do not modify, summarize, or comment.
- Do not provide suggestions or explanations.

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
    tools=[notion_tool],
    output_key='recipe_writer'
)