# AI Research Analyst

A multi-agent AI app that turns any topic into a structured, sourced research report. Three specialized agents built with CrewAI work in sequence, and a Streamlit page lets you enter a topic and read or download the result.

## Overview

Researching a topic by hand means searching, reading, comparing sources, and writing everything up. This project automates that workflow. You type a topic, and a small team of AI agents searches the web, analyzes what it finds, and writes a clean markdown report with headings, key findings, risks, opportunities, and a conclusion.

## How it works

1. **Researcher** searches the web (Tavily) and reads pages to collect recent, credible findings.
2. **Analyst** turns the findings into trends, risks, opportunities, and key takeaways.
3. **Report writer** produces the final report in markdown.

The agents run one after another, and each one receives the previous agent's output.

| Agent | Role | Tools |
|---|---|---|
| Senior Data Researcher | Finds recent facts, players, and sources on the topic | Tavily search, website scraper |
| Reporting Analyst | Identifies trends, risks, opportunities, and weak evidence | None |
| Report Writer | Writes the final structured report | None |

## Features

- Enter any topic in a simple web interface
- Live web search, so reports reflect current information
- The agents know today's date, so "recent" means recent
- Final report shown on the page, with a download button (`report.md`)
- Clear button to reset and research the next topic
- Agent steps are capped and delegation is turned off to keep runs fast and within free API quotas

## Example topics

- Future of electric vehicles in India
- 5G technology impact in India
- Latest developments in AI agents

## Tech stack

- Python
- CrewAI (multi-agent framework, JSON project configuration)
- Google Gemini (`gemini-3.1-flash-lite`) as the LLM
- Tavily Search API for web search
- Streamlit for the web interface
- uv for dependency management

## Project structure

```
ai_research_analyst/
├── app.py                 # Streamlit UI
├── crew.jsonc             # Tasks, process, and crew settings
├── agents/
│   ├── topic_senior_data_researcher.jsonc
│   ├── topic_reporting_analyst.jsonc
│   └── topic_report_writer.jsonc
├── pyproject.toml         # Dependencies
└── uv.lock                # Locked dependency versions
```

## Setup

1. Clone the repo and open the folder:

```bash
   git clone https://github.com/ommichaitanya3/ai-research-analyst.git
   cd ai-research-analyst
```

2. Install dependencies:

```bash
   uv sync
```

3. Create a `.env` file in the project root with your API keys:

```
   MODEL=gemini/gemini-3.1-flash-lite
   GEMINI_API_KEY=your_gemini_key
   TAVILY_API_KEY=your_tavily_key
```

   Get a free Gemini key at [Google AI Studio](https://aistudio.google.com/apikey) and a free Tavily key at [tavily.com](https://tavily.com).

## Run

Start the web app:

```bash
uv run streamlit run app.py
```

Then open `http://localhost:8501`, enter a topic, and click **Generate report**.

To run the crew from the terminal instead:

```bash
crewai run
```

## Configuration

- **Change the model:** edit the

# AI Research Analyst

**Live Demo:** https://ai-research-analyst-dmtw3i34g7hj7zi7fjlfpb.streamlit.app/

A multi-agent AI application that researches topics and generates structured reports using CrewAI, Google Gemini, Tavily, and Streamlit.