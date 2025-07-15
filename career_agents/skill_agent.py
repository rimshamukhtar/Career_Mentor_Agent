from agents import Agent
from model_loader import model
from tools import career_roadmap_tool


SkillAgent = Agent(
    name="Skill Builder",
    instructions="Help the user by showing a skill roadmap and job roles for their selected career field.",
    model=model,
    tools=[career_roadmap_tool]  # use the wrapped tool
)
