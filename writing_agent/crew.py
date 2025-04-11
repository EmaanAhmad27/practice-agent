import streamlit as st
from crewai import Crew
from dotenv import load_dotenv
from agents import Researcher_Agent, SEO_Expert_Agent, Content_Editor_Agent, SEO_Content_Writer_Agent
from tasks import research_task, SEO_task, Content_task, Editing_task

load_dotenv()

st.set_page_config(page_title="Content Writer Agent", layout="centered")
st.title("🧠✍️ AI Content Writing Assistant")
st.markdown("Give me a blog topic, and I’ll let your AI team handle research, SEO, writing, and editing.")

with st.sidebar:
    st.header("🧑‍💻 Meet Your AI Team")
    
    st.subheader("🔎 Researcher Agent")
    st.write("Finds up-to-date and relevant information about your topic to build a strong base.")
    
    st.subheader("📈 SEO Expert Agent")
    st.write("Analyzes SEO trends and keywords to make your content rank better on search engines.")
    
    st.subheader("✍️ SEO Content Writer Agent")
    st.write("Writes the blog using the research and SEO input, keeping it natural and engaging.")
    
    st.subheader("📝 Content Editor Agent")
    st.write("Polishes the blog by checking grammar, tone, and flow to make it ready to publish.")

# --- Main App ---
topic = st.text_input("🎯 Topic:", "")

if st.button("Create Blog Post"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("AI agents are working on your content..."):
            crew = Crew(
                agents=[Researcher_Agent, SEO_Expert_Agent, Content_Editor_Agent, SEO_Content_Writer_Agent],
                tasks=[research_task, SEO_task, Content_task, Editing_task],
                verbose=False,
            )
            result = crew.kickoff(inputs={"topic": topic})

            if isinstance(result, dict):
                result_text = result.get("output", "No content found.")
            elif isinstance(result, list):
                result_text = "\n\n".join(str(r) for r in result)
            else:
                result_text = str(result)

        st.success("Content Generated!")
        st.markdown("### 📝 Final Blog")
        st.text_area("Blog Output", result_text, height=400)
        st.download_button("Download Blog", result_text, file_name="blog.txt")
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Built by Emaan Ahmad❤️</p>", unsafe_allow_html=True)
