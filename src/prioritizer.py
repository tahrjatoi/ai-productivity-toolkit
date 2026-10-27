"""Smart Task Prioritizer using LLM scoring"""

from typing import List, Dict
import os
from dotenv import load_dotenv

load_dotenv()

def prioritize_tasks(tasks: List[Dict]) -> List[Dict]:
    """
    Score and rank tasks based on impact, urgency, and effort.
    In production this would call an LLM. For now it uses a simple heuristic
    so the project runs without an API key.
    """
    def score(task: Dict) -> float:
        impact_map = {"high": 3.0, "medium": 2.0, "low": 1.0}
        effort_map = {"low": 1.5, "medium": 1.0, "high": 0.6}
        
        impact = impact_map.get(task.get("impact", "medium"), 2.0)
        effort = effort_map.get(task.get("effort", "medium"), 1.0)
        
        # Simple urgency based on deadline presence
        urgency = 1.3 if task.get("deadline") else 1.0
        
        return impact * effort * urgency
    
    scored = []
    for t in tasks:
        t = t.copy()
        t["score"] = round(score(t), 2)
        scored.append(t)
    
    return sorted(scored, key=lambda x: x["score"], reverse=True)
