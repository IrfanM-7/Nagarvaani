from brain.gemma_brain import ask_gemma
from skills.basic_skills import get_date_time, handle_complaint

def tamil_vaani():
    print("🎙️ தமிழ்வாணி தயாராக உள்ளது!\n")
    while True:
        q = input("❓ உங்கள் கேள்வி: ").strip().lower()
        if q in ["வெளியேறு", "exit"]:
            break

        if "தேதி" in q or "நாள்" in q or "நேரம்" in q:
            reply = get_date_time()
        elif "புகார்" in q:
            reply = handle_complaint(q)
        else:
            prompt = f"நீ ஒரு தமிழ் உதவியாளர். பயனர் கேட்டார்: {q}. குறுகிய பதிலாக தமிழில் சொல்லு."
            reply = ask_gemma(prompt)

        print("🤖 தமிழ்வாணி:", reply, "\n")

if __name__ == "__main__":
    tamil_vaani()
