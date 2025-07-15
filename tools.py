class Tool:
    def __init__(self, name, func, description=""):
        self.name = name
        self.func = func
        self.description = description

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

def get_career_roadmap(field: str) -> str:
    return f"""🛠️ Roadmap for {field}:
- Learn fundamentals
- Build projects
- Get certified
- Apply for internships/jobs
"""

career_roadmap_tool = Tool(
    name="get_career_roadmap",
    func=get_career_roadmap,
    description="Returns a career skill-building roadmap for a given field."
)