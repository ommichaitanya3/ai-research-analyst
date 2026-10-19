from pathlib import Path

import streamlit as st
from crewai.project.crew_loader import load_crew

CREW_PATH = Path(__file__).parent / "crew.jsonc"


def clear_all():
    st.session_state["topic_input"] = ""
    st.session_state.pop("report", None)
    st.session_state.pop("topic", None)


st.set_page_config(page_title="AI Research Analyst")
st.title("AI research analyst")
st.caption("Enter a topic and three agents will research, analyze, and write a report.")

topic = st.text_input(
    "Topic", key="topic_input", placeholder="5G technology impact in India"
)

generate = st.button("Generate report")

if generate:
    if not topic.strip():
        st.error("Enter a topic first")
    else:
        try:
            with st.spinner("The agents are working. This can take a few minutes."):
                crew, _ = load_crew(CREW_PATH)
                result = crew.kickoff(inputs={"topic": topic.strip()})
            st.session_state["report"] = result.raw
            st.session_state["topic"] = topic.strip()
        except Exception as e:
            st.error(f"Something went wrong: {e}")

if "report" in st.session_state:
    st.divider()
    st.subheader(st.session_state["topic"])
    st.markdown(st.session_state["report"])
    st.download_button(
        "Download report.md",
        st.session_state["report"],
        file_name="report.md",
        mime="text/markdown",
    )
    st.button("Clear", on_click=clear_all)
