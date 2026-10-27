"""Daily Brief Generator"""

from typing import List, Dict
from datetime import date

def generate_daily_brief(tasks: List[Dict], notes: List[str] = None) -> str:
    """
    Create a focused daily brief from tasks and optional notes.
    """
    today = date.today().strftime("%A, %B %d")
    
    high_priority = [t for t in tasks if t.get("impact") == "high"]
    
    brief = f"""Daily Brief — {today}
{'='*40}

Focus Areas (High Impact):
"""
    for t in high_priority[:3]:
        brief += f"  • {t['title']}\n"
    
    if notes:
        brief += "\nKey Notes:\n"
        for n in notes[:3]:
            brief += f"  • {n}\n"
    
    brief += "\nTip: Protect your first 90 minutes for deep work.\n"
    return brief
