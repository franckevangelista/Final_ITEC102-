def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

def safe_int(text, default=0):
    try:
        return int(text)
    except ValueError:
        return default

print(safe_divide(10, 4))
print(safe_divide(10, 0))
print(safe_int("25"))
print(safe_int("2x5"))
print(safe_int("2x5", default=-1))
