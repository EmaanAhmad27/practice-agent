from crewai import Task
from tools import research_tool, Writing_tool, SEO_tool, Editor_tool
from agents import Researcher_Agent, SEO_Expert_Agent, Content_Editor_Agent, SEO_Content_Writer_Agent

research_task = Task(
    name="Comprehensive Topic Research",
    description="The Researcher Agent will conduct a detailed web search using Google Serper Search to gather relevant, up-to-date, and authoritative information on a topic {topic}. The agent will extract key insights, statistics, competitor content summaries, and trending subtopics.",
    expected_output= "Summary of key findings (main ideas, trends, and essential details), List of authoritative sources (with URLs for credibility), Competitor content breakdown (brief analysis of top-ranking articles), Relevant statistics & data points (to add credibility to the blog), Common audience questions & pain points (for engagement and SEO optimization)",
    tools=[research_tool],
    agent= Researcher_Agent
)

SEO_task = Task(
    name = "SEO Analysis",
    description = "The SEO Expert Agent will analyze the topic {topic} and research findings using EXA Search Web Loader to identify the most relevant keywords, search trends, and ranking strategies. The agent will ensure the content is structured for maximum search visibility, suggest keyword placements, and recommend SEO-friendly headings and meta descriptions.",
    expected_output =("List of high-ranking primary & secondary keywords (with search volume & competition level)"
                      "SEO-optimized title & meta description (for better click-through rates)"
                      "Heading structure suggestions (H1, H2, H3 based on SEO best practices)"
                      "Keyword placement recommendations (where to use them naturally)"
                      "Internal & external link recommendations (for improved content authority)"),
    tools=[SEO_tool],
    agent= SEO_Expert_Agent
    )

Content_task = Task(
    name = "SEO-Optimized Blog Drafting",
    description = "The SEO Content Writer Agent will use the research insights and SEO recommendations to draft a well-structured, engaging, and SEO-friendly blog post on the topic {topic}. The agent will ensure that the content is readable, informative, and naturally optimized for search engines while maintaining a compelling tone for the target audience.",
    expected_output = ("Complete blog draft (well-structured with a clear introduction, body, and conclusion)"
                       "Engaging introduction (hooks readers and includes primary keywords naturally)"
                       "SEO-optimized headings (H1, H2, H3 based on SEO suggestions)"
                       "Seamless keyword integration (without keyword stuffing)"
                       "Well-researched insights & examples (to add value to readers)"
                       "Internal & external links added (for improved SEO and credibility)"),
    tools=[Writing_tool],
    agent= SEO_Content_Writer_Agent
)

Editing_task = Task(
    name = "Content Polishing & SEO Refinement",
    description = "The Editor Agent will review the blog draft to improve clarity, readability, and overall flow while ensuring SEO best practices are maintained. The agent will check for grammar, spelling, tone consistency, and keyword placement, making sure the content on the topic {topic} is engaging, professional, and free of errors.",
    expected_output= "A final blog in a blog form",
    tools=[Editor_tool],
    agent= Content_Editor_Agent
)
