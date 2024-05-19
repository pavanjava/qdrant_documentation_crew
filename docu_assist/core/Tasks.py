from core.Agents import CodingAgents
from core.Tools import CodeGenerationTools
from crewai import Task


class CodingTasks:
    def __init__(self):
        self.coding_agents = CodingAgents()
        self.coding_tools = CodeGenerationTools()

    def search_task(self, agent):
        return Task(
            description=(
                "1. Prioritize the latest python code syntax, semantics "
                "& code guidelines, on {topic}.\n"
                "2. Identify the target audience, like jr engineers, "
                "mid jr engineers and sr engineers their expertise.\n"
                "3. Develop a detailed code file including "
                "the actual logic in the form of python class, key comments, def or methods etc.\n"
            ),
            expected_output="A comprehensive code file with the actual logic classes, key comments, "
                            "exception handling and def or methods etc.",
            tools=[self.coding_tools.search_tool()],
            agent=agent,
        )

    def coder_task(self, agent):
        return Task(
            description=(
                "1. Use the code plan to craft a compiled and running "
                "code on {topic}.always create class file to create the logic example: `class Sample:`\n"
                "2. Incorporate the actual logic in class, key comments, "
                "def or methods etc.\n"
                "3. The actual logic, key comments, classes, "
                "def or methods, exception handling etc. are properly named in an engaging manner.\n"
                "4. Ensure the code is structured with correct "
                "syntax, semantics, code guidelines .\n"
                "5. Proofread for any syntax, semantics, code guidelines errors and "
                "alignment with the correct details. Dont include any extra, junk, "
                "or any other informative text in the code file.\n"
            ),
            expected_output="A well-written python code file 'code.py' format, ready for compile and run.",
            agent=agent,
            async_execution=False,
            output_file='code.py'  # Example of output customization
        )

    def editorial_task(self, agent):
        return Task(
            description=("Proofread the given code in code.py for "
                         "any syntax, semantics, code guidelines errors. Remove any "
                         "irrelevant things like extra text, junk text, special chars like ``` "
                         "or any other informative text in the code file."),
            expected_output="A code file correct format, ready for running .",
            agent=agent
        )
