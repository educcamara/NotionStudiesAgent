
from google.adk.agents.llm_agent import Agent
from notion_studies.notion_tool import notion_tool

# Recipe File Creator Agent
recipe_file_creator = Agent(
    model='gemini-3-flash-preview',
    name='recipe_file_creator',
    description='Creates a new recipe note in Notion with the same template structure as existing recipes in Personal Home/Recipes. Only populates the template, does not fill in recipe content.',
    instruction="""
You are a deterministic recipe file creator agent.

The previous step couldn't find the recipe in Notion:
{recipe_checker}

Your task is to:
1. Check the structure of existing recipes in Personal Home/Recipes (e.g., Ingredients, Preparation, Observations).
2. Create a new recipe note at Personal Home/Recipes/<New Recipe Name> with only the template structure, leaving all fields empty (except the title, that will be the recipe name).

Operational Rules:
- Do not fill in any recipe content.
- Do not modify, summarize, or comment.
- Do not provide suggestions or explanations.

If the note is successfully created, return:
{
    "status": "created",
    "file_path": "Personal Home/Recipes/<New Recipe Name>"
}

If there is an error, return:
{
    "status": "error"
}

Do not include any text outside the JSON response.
    """,
    tools=[notion_tool],
    output_key='recipe_file_creator'
)