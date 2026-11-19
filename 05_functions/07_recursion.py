def factorial(n):
    if n <= 1:                  # base case
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("5! =", factorial(5))
print("10! =", factorial(10))
for i in range(10):
    print(fibonacci(i), end=" ")
print()
