from core.Agents import CodingAgents
from core.Tasks import CodingTasks
from crewai import Crew, Process
from phoenix.trace.langchain import LangChainInstrumentor
import phoenix as px
import warnings

warnings.filterwarnings('ignore')

session = px.launch_app()
LangChainInstrumentor().instrument()

coding_agents = CodingAgents()
coding_tasks = CodingTasks()

search_agent = coding_agents.search_agent()
code_agent = coding_agents.coder_agent()
editor_agent = coding_agents.coding_editor_agent()

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[search_agent, code_agent, editor_agent],
    tasks=[coding_tasks.search_task(agent=search_agent), coding_tasks.coder_task(agent=code_agent),
           coding_tasks.editorial_task(agent=editor_agent)],
    process=Process.sequential,  # Optional: Sequential task execution is default
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={"topic": "insert data into qdrant using python."})
print(px.active_session().url)
print(result)
