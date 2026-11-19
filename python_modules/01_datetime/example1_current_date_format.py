from datetime import datetime

now = datetime.now()
print("Raw:", now)
print("Date:", now.strftime("%B %d, %Y"))        # November 19, 2026
print("Weekday:", now.strftime("%A"))
print("Time (12h):", now.strftime("%I:%M %p"))
print("Short:", now.strftime("%m/%d/%y"))
print("Year:", now.year, "| Month:", now.month, "| Day:", now.day)
