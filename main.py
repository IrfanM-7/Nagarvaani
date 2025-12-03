# main.py
from voice_bot.record import record_audio
from voice_bot.transcribe import transcribe_tamil
from voice_bot.speak import speak_text
from voice_bot.ai_response import get_ai_reply

print("🎙️ பேச தொடங்குங்கள்...")
record_audio("input.wav")

print("🧠 உரையை மாற்றுகிறது...")
text = transcribe_tamil("input.wav").strip()
print("❓ உங்கள் கேள்வி:", text)

if not text:
    print("⚠️ ஒலி கேட்கவில்லை. மீண்டும் முயற்சிக்கவும்.")
else:
    print("🤔 யோசிக்கிறது...")
    reply = get_ai_reply(text).strip()

    print("💬 தமிழ்வாணி:", reply)
    speak_text(reply)
