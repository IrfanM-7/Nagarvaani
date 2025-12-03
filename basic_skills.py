import datetime

def get_date_time():
    now = datetime.datetime.now()
    return f"இன்று {now.strftime('%A, %d %B %Y')} {now.strftime('%I:%M %p')}."

def handle_complaint(text):
    # very simple civic complaint mock
    with open("data/complaints.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")
    return "உங்கள் புகார் பதிவு செய்யப்பட்டது. நன்றி!"
