from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
import os


class CodingAgents:
    def __init__(self):
        _ = load_dotenv(find_dotenv())
        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")  # platform.openai key
        os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")  # serper key to search web
        self.llm = ChatOpenAI(model=os.getenv("OPENAI_LLM"), temperature=0.3)

    def search_agent(self):
        return Agent(
            role="Coding Content Searcher",
            goal="search factually accurate coding content on {topic}",
            backstory="You're working on coding a python file "
                      "about the topic: {topic}."
                      "You collect information that helps the "
                      "user by directly running the python content and file "
                      "and make informed decisions. "
                      "Your work is the basis for "
                      "the Senior Python Coder to write the python file on this topic. ",
            allow_deligation=False,
            verbose=True

        )

    def coder_agent(self):
        return Agent(
            role="Senior Python Coder",
            goal="Write factually accurate "
                 "and runnable python code about the topic: {topic}",
            backstory="You're working on a writing "
                      "a new python code about the topic: {topic}. "
                      "You base your coding on the work of "
                      "the Coding Content Searcher, who provides an outline "
                      "and relevant context about the topic. "
                      "You follow the main objectives and "
                      "direction of the outline, also always use python classes"
                      "as provide by the Coding Content Searcher. "
                      "You also provide accurate python file that can run directly by the user"
                      "and back them up with appropriate comments "
                      "provide by the Coding Content Searcher.",
            allow_delegation=False,
            verbose=True
        )

    def coding_editor_agent(self):
        return Agent(
            role="Senior Coding Editor",
            goal="Edit a given code file to align with "
                 "the writing style of the python syntax and semantics. ",
            backstory="You are an editor who receives a code file "
                      "from the Senior Python Coder. "
                      "Your goal is to review the code content "
                      "to ensure that it follows syntax, semantics, coding guidelines and best practices,"
                      "provides balanced viewpoints "
                      "when providing opinions or assertions, "
                      "and also avoids major deviations in code guidelines "
                      "or syntax and semantics when possible."
                      "Note: Always make sure the tokens are under 8192 while passing to next agent or task",
            allow_delegation=False,
            verbose=True
        )
