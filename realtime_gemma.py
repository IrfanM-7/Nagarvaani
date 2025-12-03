import subprocess
import datetime
import sys
import os

# ✅ Ensure console and Python use UTF-8 on Windows
os.system("chcp 65001 >nul")
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# ✅ Get real date/time
today = datetime.datetime.now()
weekday_tamil = {
    "Monday": "திங்கள்",
    "Tuesday": "செவ்வாய்",
    "Wednesday": "புதன்",
    "Thursday": "வியாழன்",
    "Friday": "வெள்ளி",
    "Saturday": "சனி",
    "Sunday": "ஞாயிறு"
}
month_tamil = {
    "January": "ஜனவரி", "February": "பிப்ரவரி", "March": "மார்ச்",
    "April": "ஏப்ரல்", "May": "மே", "June": "ஜூன்",
    "July": "ஜூலை", "August": "ஆகஸ்ட்", "September": "செப்டம்பர்",
    "October": "அக்டோபர்", "November": "நவம்பர்", "December": "டிசம்பர்"
}

eng_day = today.strftime("%A")
eng_month = today.strftime("%B")
date_str = f"{weekday_tamil.get(eng_day, eng_day)}, {today.day} {month_tamil.get(eng_month, eng_month)} {today.year}"
time_str = today.strftime("%I:%M %p")

# ✅ Build context for Gemma
prompt = f"""நீ ஒரு தமிழ் செயற்கை நுண்ணறிவு உதவியாளர்.
இன்றைய தேதி: {date_str}
நேரம்: {time_str}

உன் பணி:
1️⃣ எப்போதும் தமிழில் மட்டும் பேசு.
2️⃣ எளிய, தெளிவான, இயல்பான தமிழ் வாக்கியத்தில் பதிலளி.
3️⃣ வாக்கியம் “இன்று ...” என்று தொடங்க வேண்டும்.
4️⃣ மிகச் சுருக்கமாகவும் உண்மையாகவும் பதில் கொடு.
"""

# ✅ Get user input
user_q = input("❓ உங்கள் கேள்வியை தமிழில் சொல்லுங்கள்: ").strip()

# ✅ Combine prompt
full_prompt = f"{prompt}\n\nபயனர்: {user_q}\nபதில் (தமிழில், ஒரு குறுகிய வாக்கியமாக):"

# ✅ Call Gemma model
result = subprocess.run(
    ["ollama", "run", "gemma"],
    input=full_prompt.encode("utf-8"),
    capture_output=True
)

# ✅ Print only Tamil reply
response = result.stdout.decode("utf-8", errors="ignore").strip()
if response:
    print(f"\n{response}")
else:
    print("\nபதில் பெற முடியவில்லை. தயவுசெய்து மீண்டும் முயற்சிக்கவும்.")
