from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from notion_studies.notion_tool import notion_tool

recipe_researcher = Agent(
    model='gemini-3-flash-preview',
    name='recipe_researcher',
    description='Searches for recipes online and saves them to Notion.',
    instruction="""
    You are a recipe researcher.
    When a recipe is not found in Notion, your role is to:
    1. Search for the recipe on the internet using the search tool.
    2. Compile the ingredients and preparation method into a clear format.
    3. Create a new page in Notion at the path "Personal Home/Recipes" with the recipe name.
    4. Save the recipe content to this new page.
    
    You must only create the recipe content, not any other text. The recipe content should be concise and well-structured, including a list of ingredients and step-by-step preparation instructions.
    """,
    tools=[google_search, notion_tool],
    output_key='recipe_researcher'
)

