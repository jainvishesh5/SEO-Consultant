from crewai import Agent , Task , Crew , Process
from crewai_tools import SerperDevTool , ScrapeWebsiteTool

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

class SEOCrews:
    @staticmethod
    def create_auditor_crew()-> Crew:
        agent = Agent(
            role = "SEO Auditor",
            goal = "Analyse the target website {website} for structural optimisation gaps and provide a detailed report on the findings.",
            backstory = "An expert in core web vitals, DOM architectures, metadata indexing, and crawl budget optimizations.",
            tools = [scrape_tool],
            verbose = True
        )

        task = Task(
            description = "Scrape and analyse the structural layout ,  headers , and performance bottlenecks of {website}.",
            expected_output = "A comprehensive report detailing the structural optimisation gaps of the target website.",
            agent = agent
        )
        return Crew(agents = [agent] , tasks = [task] , process = Process.sequential)
    
    @staticmethod
    def create_competitor_crew()->Crew:
        agent = Agent(
            role = "Competitor Researcher",
            goal = "Identify and analyse the top competitors of {website} in the SEO landscape, providing insights into their strategies and performance.",
            backstory = "A specialist in competitive analysis, keyword research, and backlink profiling.",
            tools = [search_tool],
            verbose = True
        )

        task = Task(
            description = "Conduct a comprehensive competitor analysis for {website}, identifying key competitors, their SEO strategies, and performance metrics.",
            expected_output = "A detailed report outlining the top competitors of the target website, their SEO strategies, and performance insights.",
            agent = agent
        )
        return Crew(agents = [agent] , tasks = [task] , process = Process.sequential)
    
    @staticmethod
    def create_synthesizer_crew()->Crew:
        agent = Agent(
            role = "SEO Synthesizer",
            goal = "Synthesize the findings from the SEO audit and competitor analysis to create a comprehensive final report with actionable recommendations for {website}.",
            backstory = "An expert in data synthesis, report writing, and strategic SEO planning.",
            tools = [],
            verbose = True
        )

        task = Task(
            description=(
                "Review the comprehensive data metrics compiled for {website}.\n\n"
                "### Core Technical Web Audit:\n{audit_results}\n\n"
                "### Competitor Analysis & Keyword Footprints:\n{competitor_list}\n\n"
                "Synthesize an exhaustive, production-grade 3-page SEO Strategy Report utilizing the data blocks above."
            ),
            expected_output = "A comprehensive final report that synthesizes the findings from both the SEO audit and competitor analysis, providing clear and actionable recommendations for {website}.",
            agent = agent
        )
        return Crew(agents = [agent] , tasks = [task] , process = Process.sequential ,max_rpm = 30)
