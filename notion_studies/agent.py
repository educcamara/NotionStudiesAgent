from google.adk.agents import SequentialAgent
from google.adk.apps import App
from google.adk.plugins import LoggingPlugin

from notion_studies.agents.recipe_checker import recipe_checker
from notion_studies.agents.decision_agent import decision_agent

root_agent = SequentialAgent(
    name='root_agent',
    sub_agents=[
        recipe_checker,
        decision_agent,
    ]
)

app = App(
    name="notion_studies",
    root_agent=root_agent,
    plugins=[LoggingPlugin()]
)