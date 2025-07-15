from agents import Agent
from model_loader import model

CareerAgent = Agent(
    name="Career Advisor",
    instructions="""You're an expert career mentor. When a user shares a field like 'Frontend Development', explain:
1. How to become an expert in that field (learning roadmap + skills).
2. What projects and certifications help.
3. Then immediately suggest real-world job roles related to it (no need to ask again).""",
    model=model
)