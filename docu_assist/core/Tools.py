from crewai_tools import SerperDevTool, ScrapeWebsiteTool


class CodeGenerationTools:
    def __init__(self):
        self.docs_scrape_tool = ScrapeWebsiteTool(
            website_url="https://qdrant.tech/documentation/concepts/"
        )

    def search_tool(self):
        return SerperDevTool()

    def scrape_tool(self):
        return ScrapeWebsiteTool()