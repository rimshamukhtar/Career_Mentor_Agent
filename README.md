# 👩‍🏫 Career Mentor Agent

Plan your professional future with AI-powered career roadmaps!

---

## 📌 Overview
This project is a multi-agent AI application built using the **OpenAI Agent SDK** and **Chainlit**. The Career Mentor Agent helps users map out their career journey in any field with intelligent suggestions and a structured plan.

- 🎓 **MentorAgent** — Analyzes user queries and generates detailed career roadmaps.
- 🛠️ **get_career_roadmap Tool** — Provides a step-by-step skill-building path for various professions.

Unlike multi-turn dialogues, this project uses **one-shot execution**, meaning you get your full roadmap in a single message!

---

## 🔧 Tools Used
- **OpenAI Agent SDK** — For defining agent and tool behavior
- **Chainlit** — Real-time interactive UI
- **dotenv** — For secure API key handling

---

## 📂 Folder Structure

career_mentor_agent/
├── main.py # Orchestration logic + Chainlit UI
├── model_loader.py # LLM model configuration (LiteLLM/OpenAI)
├── tools.py # Tool: get_career_roadmap
├── career_agents/
│ └── mentor_agent.py # Mentor agent with tool access
├── .env # For API keys
└── README.md # You're reading this!

---

## 🚀 How to Run the Project

### 1. Clone the Repository

git clone https://github.com/your-username/career-mentor-agent.git
cd career_mentor_agent

---

OPENAI_API_KEY=your_openai_key_here


## Start chainlit
chainlit run main.py

---

## Example Prompt
"I want to become a data scientist"
"How to enter the UI/UX design field?"
"Give me a career roadmap for DevOps"
"Suggest a plan to learn cloud computing"

---

## 🌐 Tech Stack
Python 3.10+

OpenAI Agent SDK

Chainlit

dotenv

---

🙋‍♀️**Built By**

**Rimsha Mukhtar**
