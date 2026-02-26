from google.adk.agents import ParallelAgent

from notion_studies.agents.recipe_file_creator import recipe_file_creator
from notion_studies.agents.recipe_researcher import recipe_researcher

parallel_agent = ParallelAgent(
    name="parallel_agent",
    description="""
    Agent that runs both the recipe file creator (to create the recipe file in Notion) and the recipe writer (to fill the recipe content in the created file) in parallel.
    """,
    sub_agents=[
        recipe_researcher,
        recipe_file_creator,
    ]
)