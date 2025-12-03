import whisper

model = whisper.load_model("small")  # You can change to 'base' or 'tiny' if slow

def transcribe_tamil(audio_path):
    print("🧠 Transcribing Tamil speech...")
    result = model.transcribe(audio_path, language="ta")
    text = result["text"]
    print(f"🗣️ You said: {text}")
    return text
