#!/usr/bin/env python3
"""AI Productivity Toolkit - Entry point"""

from src.prioritizer import prioritize_tasks
from src.brief import generate_daily_brief

def main():
    print("AI Productivity Toolkit")
    print("=" * 40)
    
    # Example: prioritize sample tasks
    sample_tasks = [
        {"title": "Ship personal RAG assistant", "deadline": "2026-10-30", "impact": "high", "effort": "medium"},
        {"title": "Review Aspire assignments", "deadline": "2026-10-28", "impact": "high", "effort": "low"},
        {"title": "Clean up GitHub profile", "deadline": "2026-10-27", "impact": "medium", "effort": "low"},
        {"title": "Learn multi-agent patterns", "deadline": "2026-11-05", "impact": "high", "effort": "high"},
    ]
    
    print("\nPrioritized Tasks:")
    ranked = prioritize_tasks(sample_tasks)
    for i, task in enumerate(ranked, 1):
        print(f"{i}. {task['title']} (score: {task.get('score', 'N/A')})")

if __name__ == "__main__":
    main()
