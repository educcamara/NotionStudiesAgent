from google.adk.agents import SequentialAgent

from notion_studies.agents.aggregator_agent import aggregator_agent
from notion_studies.agents.parallel_agent import parallel_agent

sequential_agent = SequentialAgent(
    name="sequential_agent",
    description="""
    Recipe creation pipeline. Runs only when a recipe is NOT found in Notion.
    Executes in order:
      1. parallel_agent — concurrently researches the recipe online (recipe_researcher) and creates the empty Notion file (recipe_file_creator).
      2. aggregator_agent — writes the researched recipe content into the created Notion file.
    """,
    sub_agents=[
        parallel_agent,
        aggregator_agent
    ]
)