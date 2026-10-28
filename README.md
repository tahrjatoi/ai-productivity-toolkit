<div align="center">

# AI Productivity Toolkit

**Practical AI-powered tools that help developers and knowledge workers focus on high-leverage work.**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## Overview

Most productivity tools are either too rigid or too generic.  
This toolkit uses LLMs to adapt to *your* context and deliver actionable recommendations instead of static lists.

Built for engineers who want AI to reduce cognitive load — not add more noise.

---

## Features

| Tool | Description |
|------|-------------|
| **Smart Task Prioritizer** | Scores and ranks tasks based on urgency, impact, and effort using AI |
| **Daily Brief Generator** | Summarizes calendar, todos, and notes into a focused morning brief |
| **Meeting Notes Cleaner** | Transforms messy transcripts into structured action items and decisions |
| **Focus Session Planner** | Creates realistic deep-work blocks based on energy patterns and priorities |

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/tahrjatoi/ai-productivity-toolkit.git
cd ai-productivity-toolkit

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Add your OpenAI / Grok / Anthropic API key

# 4. Run
python main.py
```

---

## Project Structure

```text
ai-productivity-toolkit/
├── src/
│   ├── prioritizer.py      # Task scoring engine
│   ├── brief.py            # Daily brief generator
│   ├── notes_cleaner.py    # Meeting notes processor
│   └── planner.py          # Focus block generator
├── examples/
│   └── sample_tasks.json
├── requirements.txt
├── .env.example
└── main.py
```

---

## Example Usage

```python
from src.prioritizer import prioritize_tasks

tasks = [
    {"title": "Finish RAG pipeline", "deadline": "2026-10-28", "impact": "high"},
    {"title": "Reply to emails", "deadline": "2026-10-27", "impact": "medium"},
]

ranked = prioritize_tasks(tasks)
print(ranked)
```

---

## Tech Stack

- **Python 3.10+**
- LangChain / OpenAI-compatible APIs (OpenAI, Grok, Anthropic)
- Clean modular design for easy extension

---

## Roadmap

- [ ] Web UI (FastAPI + React)
- [ ] Calendar integration (Google / Outlook)
- [ ] Persistent memory of user preferences
- [ ] Multi-user / team support

---

## Author

**Tahir Jatoi** — AI Engineer  
Building production-ready intelligent systems.

- GitHub: [tahrjatoi](https://github.com/tahrjatoi)
- LinkedIn: [Tahir Jatoi](https://www.linkedin.com/in/tahrjatoi)

---

<div align="center">

*Built to help you think less about what to do next — and more about doing it well.*

</div>
