from google.adk.agents.llm_agent import Agent
from google.adk.models import Gemini
from google.adk.tools import google_search
from notion_studies.notion_tool import notion_tool
from notion_studies.util.retry_config import retry_config

recipe_researcher = Agent(
    name='recipe_researcher',
    model=Gemini(
        model='gemini-2.5-flash',
        retry_options=retry_config
    ),
    description='Searches for recipes online.',
    instruction="""
    You are a recipe researcher.
    Your goal is to find a recipe online and format it clearly.
    
    Previously, the recipe checker agent attempted to find the recipe in Notion but was unsuccessful:
    {recipe_checker}

    Your task is to find the recipe online and extract the title, ingredients, and instructions. You should:
    1.  Search the internet for the recipe using the available search tool.
    2.  Once you find a suitable recipe, extract the following information:
        *   **Title**: The name of the recipe.
        *   **Ingredients**: A list of all ingredients.
        *   **Instructions**: A step-by-step guide on how to prepare the recipe.
    3.  Format the output in a clear and organized manner, using markdown for readability. For example:

        **Mousse de Maracujá**

        **Ingredientes:**
        *   1 lata de leite condensado
        *   1 lata de creme de leite
        *   1 lata de suco de maracujá concentrado

        **Modo de Preparo:**
        1.  Bata todos os ingredientes no liquidificador.
        2.  Despeje em um refratário e leve à geladeira por pelo menos 4 horas.
        3.  Sirva gelado.
    """,
    tools=[google_search],
    output_key='recipe_researcher'
)
