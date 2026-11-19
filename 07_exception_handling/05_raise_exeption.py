def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age is unrealistic")
    return age

for test in (25, -5, 200):
    try:
        print("Valid age:", set_age(test))
    except ValueError as e:
        print("Invalid:", e)
