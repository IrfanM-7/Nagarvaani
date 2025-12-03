from brain.gemma_brain import ask_gemma
from skills.basic_skills import get_date_time, handle_complaint

def tamil_vaani():
    print("🎙️ தமிழ்வாணி தயாராக உள்ளது!\n")

    while True:
        q = input("❓ உங்கள் கேள்வி: ").strip()
        if not q:
            continue
        if q in ["வெளியேறு", "exit", "quit"]:
            print("👋 வணக்கம்!")
            break

        if "நாள்" in q or "நேரம்" in q or "தேதி" in q:
            ans = get_date_time()
        elif "புகார்" in q:
            ans = handle_complaint()
        else:
            ans = ask_gemma(q)

        print("🤖 தமிழ்வாணி:", ans, "\n")
