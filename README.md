# AI Productivity Toolkit

A collection of practical AI-powered tools designed to boost personal productivity for developers and knowledge workers.

## Features

- **Smart Task Prioritizer** — Score and rank your tasks using AI based on urgency, impact, and effort
- **Daily Brief Generator** — Summarize your calendar, todos, and notes into a focused morning brief
- **Meeting Notes Cleaner** — Turn messy meeting transcripts into structured action items
- **Focus Session Planner** — Generate realistic deep-work blocks based on your energy patterns

## Quick Start

```bash
pip install -r requirements.txt
cp .env.example .env   # Add your OpenAI / Grok / Anthropic key
python main.py
```

## Project Structure

```
ai-productivity-toolkit/
├── src/
│   ├── prioritizer.py      # Task scoring engine
│   ├── brief.py            # Daily brief generator
│   ├── notes_cleaner.py    # Meeting notes processor
│   └── planner.py          # Focus block generator
├── examples/
│   └── sample_tasks.json
├── requirements.txt
└── main.py
```

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

## Why This Exists

Most productivity tools are either too rigid or too generic. This toolkit uses LLMs to adapt to *your* context and give you actionable recommendations instead of just lists.

---

Built with by Tahir Jatoi · AI Engineer
