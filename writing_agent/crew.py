import streamlit as st
from crewai import Crew, LLM
from dotenv import load_dotenv
from agents import Researcher_Agent, SEO_Expert_Agent, Content_Editor_Agent, SEO_Content_Writer_Agent
from tasks import research_task, SEO_task, Content_task, Editing_task
import os

load_dotenv()

llm = LLM(
    api_key=os.getenv("APIKey"),
    model="gemini/gemini-1.5-flash"
)

st.set_page_config(page_title="Content Writer Agent", layout="centered")
st.title("✍️ Content Writing Assistant")
st.markdown("Enter a topic and let your team of AI agents do the research, SEO, writing, and editing for you!")

topic = st.text_input("Enter a blog topic:", "")

if st.button("Generate Content"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Working on it..."):
            crew = Crew(
                agents=[Researcher_Agent, SEO_Expert_Agent, Content_Editor_Agent, SEO_Content_Writer_Agent],
                tasks=[research_task, SEO_task, Content_task, Editing_task],
                verbose=False,
            )
            result = crew.kickoff(inputs={"topic": topic})
            st.success("Content Generated!")
            st.write(result)
