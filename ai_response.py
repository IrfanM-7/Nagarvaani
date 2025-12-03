import subprocess
import datetime

def get_ai_reply(user_text: str) -> str:
    """Decide response or ask Gemma for Tamil reply."""

    # Smart skill detection
    q = user_text.lower()
    if "நாள்" in q or "தேதி" in q or "நேரம்" in q:
        now = datetime.datetime.now()
        return f"இன்று {now.strftime('%A, %d %B %Y')}."
    elif "புகார்" in q or "complaint" in q:
        return "உங்கள் புகார் பதிவு செய்யப்பட்டது. நன்றி!"
    else:
        # Ask Gemma via Ollama
        prompt = f"""
        நீ ஒரு தமிழ் உதவியாளர். பயனர் கேட்டார்: {user_text}.
        குறுகிய, சரியான பதிலாக தமிழில் சொல்லு.
        """
        try:
            result = subprocess.run(
                ["ollama", "run", "gemma"],
                input=prompt.encode("utf-8"),
                capture_output=True
            )
            return result.stdout.decode("utf-8", errors="ignore").strip()
        except Exception as e:
            return f"⚠️ Gemma பிழை: {e}"
