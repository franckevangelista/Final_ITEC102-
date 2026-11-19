def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate(op, a, b):
    if op == "+": return add(a, b)
    elif op == "-": return subtract(a, b)
    elif op == "*": return multiply(a, b)
    elif op == "/": return divide(a, b)
    return "Unknown operation"

print(calculate("+", 12, 8))
print(calculate("/", 12, 0))
print("GCD of 48 and 18:", gcd(48, 18))
print("Is 97 prime?", is_prime(97))
print("Is 91 prime?", is_prime(91))