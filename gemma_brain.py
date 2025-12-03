import subprocess

def ask_gemma(prompt: str) -> str:
    """Send Tamil prompt to Gemma and return reply."""
    try:
        result = subprocess.run(
            ["ollama", "run", "gemma"],
            input=prompt.encode("utf-8"),
            capture_output=True
        )
        return result.stdout.decode("utf-8", errors="ignore").strip()
    except Exception as e:
        return f"⚠️ Gemma பிழை: {e}"
