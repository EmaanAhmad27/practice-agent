from crewai import Crew, LLM
from dotenv import load_dotenv
from agents import Researcher_Agent, SEO_Expert_Agent, Content_Editor_Agent, SEO_Content_Writer_Agent
from tasks import research_task, SEO_task, Content_task, Editing_task
import os
load_dotenv()

llm = LLM(
    api_key = os.getenv("APIKey"),
    model = "gemini/gemini-1.5-flash"
)

crew = Crew(
    agents = [Researcher_Agent, SEO_Expert_Agent, Content_Editor_Agent, SEO_Content_Writer_Agent],
    tasks = [research_task, SEO_task, Content_task, Editing_task],
    verbose = False,
)
result = crew.kickoff(inputs= {"topic": 'what is malnutrition?'})
print (result)
