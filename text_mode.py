from voice_bot.ai_response import get_ai_reply

while True:
    q = input("❓ உங்கள் கேள்வி: ")
    if q.lower() in ["exit", "வெளியேறு"]:
        break
    print("🤖 தமிழ்வாணி:", get_ai_reply(q))
