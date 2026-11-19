number = 4827

last_digit = number % 10
remaining = number // 10
print("Last digit:", last_digit, "| Remaining:", remaining)

# sum of the four digits
total = (number // 1000) + (number // 100 % 10) + (number // 10 % 10) + (number % 10)
print("Sum of digits:", total)

# seconds -> hours, minutes, seconds
seconds = 98765
hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60
print(f"{seconds} seconds = {hours}h {minutes}m {secs}s")
