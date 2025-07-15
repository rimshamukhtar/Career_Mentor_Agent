from agents import Agent
from model_loader import model

JobAgent = Agent(
    name="Job Recommender",
    instructions="Provide some real-world job roles and titles related to the chosen field.",
    model=model
)