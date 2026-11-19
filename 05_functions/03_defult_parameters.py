def power(base, exponent=2):
    return base ** exponent

print(power(5))        # 25  (uses default exponent)
print(power(2, 8))     # 256

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Ana"))
print(greet("Ben", "Good morning"))
