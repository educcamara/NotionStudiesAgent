
from google.adk.agents.llm_agent import Agent
from google.adk.models import Gemini

from notion_studies.notion_tool import notion_tool
from notion_studies.util.retry_config import retry_config

# Recipe File Creator Agent
recipe_file_creator = Agent(
    name='recipe_file_creator',
    model=Gemini(
        model='gemini-2.5-flash',
        retry_options=retry_config
    ),
    description='Creates a new recipe note in Notion with the same template structure as existing recipes in Personal Home/Recipes. Only populates the template, does not fill in recipe content.',
    instruction="""
    You are a deterministic recipe file creator agent.

    The previous step couldn't find the recipe in Notion:
    {recipe_checker}

    Your task is to create a new recipe page at Personal Home/Recipes/<Recipe Name> using this EXACT template structure — do not read or inspect existing recipes:

    Page title: <Recipe Name>
    Blocks to create (in order):
    1. Heading 2: "Ingredientes"
    2. Paragraph: (empty)
    3. Heading 2: "Modo de Preparo"
    4. Paragraph: (empty)
    5. Heading 2: "Observações"
    6. Paragraph: (empty)

    Steps:
    1. Find the page ID of "Personal Home/Recipes" using API-post-search.
    2. Create a new child page inside it using API-post-page with the blocks above.
    
    Operational Rules:
    - Do not fill in any recipe content.
    - Do not modify, summarize, or comment.
    - Do not provide suggestions or explanations.
    - DO NOT create a new "Recipes" page. It MUST already exist. Your only task is to create a new note with the same template structure as the existing recipes, but with empty fields.

    If successful, return:
    {"status": "created", "file_path": "Personal Home/Recipes/<Recipe Name>"}

    If error, return:
    {"status": "error"}

    Do not include any text outside the JSON response.
    """,
    tools=[notion_tool()],
    output_key='recipe_file_creator'
)