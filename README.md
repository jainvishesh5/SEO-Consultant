
# Parallel Multi-Agent SEO Analysis Engine 🚀

An advanced, asynchronous AI agent orchestration framework built with **CrewAI Flows**, **Python 3.12**, and **Streamlit**. 

Unlike standard sequential multi-agent chains that suffer from compounding network latency bottlenecks, this system executes deep website technical auditing and live Google competitive intelligence gathering **concurrently in parallel** using non-blocking asynchronous worker channels.

---

## 🏗️ System Architecture & Directed Acyclic Graph (DAG)

The engine organizes complex AI workflows into deterministic, event-driven state transitions rather than loose, linear scripts:

1. **State Initialization (`state.py`):** Establishes a strict, type-safe data model container using Pydantic to maintain structured context throughout execution.
2. **Parallel Fan-Out (`flow.py`):** Leverages `asyncio.gather()` to launch two standalone network-bound agent teams concurrently:
   * **The Technical SEO Auditor Crew:** Scrapes the target URL to extract DOM structure, metadata indexing, performance bottlenecks, and validation flaws.
   * **The Competitor Researcher Crew:** Hits the Google search landscape programmatically via Serper.dev API to profile domain footprints, market share, and shared high-value keyword targets.
3. **Resiliency Guardrails (`crews.py`):** Configures strict `max_rpm=30` request-per-minute limits directly across the multi-agent instances to avoid concurrent thread traffic from causing `429 Too Many Requests` API rate-limit crashes.
4. **Data Fan-In & Synthesis (`flow.py`):** Listens for the successful structural return of both parallel branches, map-reduces the collective findings back into the centralized state, and passes the context to a senior **SEO Synthesizer Crew** to output a coherent, data-validated marketing strategy.
5. **Interactive UI (`main.py`):** An intuitive Streamlit interface allowing users to inject credentials, map targeted web domains, and review markdown strategy reports on the fly.

---

## 🛠️ Project File Mapping

* `state.py`: Houses the centralized Pydantic state machine (`SEOState`) tracking cross-agent execution memory.
* `crews.py`: Defines individual agent personas, backstories, tools (ScrapeWebsiteTool & SerperDevTool), tasks, and strict execution parameters.
* `flow.py`: The non-blocking execution pipeline orchestrated using event-driven `@start()` and `@listen()` decorators.
* `main.py`: The presentation layer managing secrets injection, configuration bindings, and local web app hosting.

---

## 🚀 Local Installation & Quick Start

### Prerequisites
* **Operating System:** Linux / macOS / WSL (Windows Subsystem for Linux)
* **Runtime:** Python 3.12 (Standard Stable Production Release)

### 1. Clone & Navigate to the Repository
```bash
git clone [https://github.com/jainvishesh5/SEO-Consultant.git](https://github.com/jainvishesh5/SEO-Consultant.git)
cd SEO-Consultant

```

### 2. Set Up a Clean Virtual Environment Sandbox

```bash
python3.12 -m venv SEOenv
source SEOenv/bin/activate

```

### 3. Install Fully Compliant Project Dependencies

```bash
pip install -r requirements.txt

```

### 4. Boot Up the Interactive Application Dashboard

```bash
streamlit run main.py

```

---

## 🔑 API Key Prerequisites

To initiate the live web-discovery workflows, the dashboard requires input keys for:

1. **OpenAI API Key:** Powers the primary reasoning capabilities of the agents via `gpt-4o-mini`.
2. **Serper.dev API Key:** Provides programmatic, ultra-fast access to live Google Search indices for competitor profiling.
