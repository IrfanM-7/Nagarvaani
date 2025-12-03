# voice_bot/transcribe.py
import whisper

_model = None

def get_model(name="small"):
    global _model
    if _model is None:
        _model = whisper.load_model(name)
    return _model

def transcribe_tamil(path="input.wav"):
    model = get_model("medium")
    res = model.transcribe(path, language="ta")
    return res.get("text","").strip()
