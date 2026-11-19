from datetime import datetime

raw_dates = ["2026-10-01", "2026-11-20", "2026-09-15"]
parsed = []
for text in raw_dates:
    parsed.append(datetime.strptime(text, "%Y-%m-%d"))

earliest = parsed[0]
for d in parsed:
    if d < earliest:
        earliest = d
print("Earliest:", earliest.strftime("%B %d, %Y"))

user_text = "05/11/2026"                     # day/month/year
d = datetime.strptime(user_text, "%d/%m/%Y")
print(d.strftime("%A"), "->", "weekend" if d.weekday() >= 5 else "weekday")
