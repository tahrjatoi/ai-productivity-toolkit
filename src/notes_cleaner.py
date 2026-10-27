"""Meeting Notes Cleaner"""

def clean_meeting_notes(raw_text: str) -> Dict:
    """
    Turn messy meeting notes into structured output.
    Placeholder implementation — replace with LLM call for production.
    """
    lines = [l.strip() for l in raw_text.split("\n") if l.strip()]
    
    return {
        "summary": lines[0] if lines else "No content",
        "action_items": [l for l in lines if l.lower().startswith(("todo", "action", "-", "*"))],
        "decisions": [l for l in lines if "decid" in l.lower() or "agreed" in l.lower()],
        "raw_length": len(raw_text),
    }
