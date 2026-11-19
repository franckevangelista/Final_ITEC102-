from datetime import date, timedelta

today = date(2026, 11, 5)
deadline = date(2026, 12, 15)

remaining = deadline - today                  # a timedelta object
print("Days until deadline:", remaining.days)
print("Weeks:", remaining.days // 7)

print("30 days from today:", today + timedelta(days=30))
print("One week ago:", today - timedelta(weeks=1))

birthday = date(2005, 3, 20)
age_in_days = (today - birthday).days
print("Age in years:", age_in_days // 365)
