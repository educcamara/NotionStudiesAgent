from google.adk.agents import SequentialAgent

from notion_studies.agents.aggregator_agent import aggregator_agent
from notion_studies.agents.parallel_agent import parallel_agent

sequential_agent = SequentialAgent(
    name="Sequential Agent",
    description="""
    Agent that runs the recipe researcher, then the recipe file creator, and finally the aggregator agent sequentially to complete the recipe saving process in Notion.
    """,
    sub_agents=[
        parallel_agent,
        aggregator_agent
    ]
)