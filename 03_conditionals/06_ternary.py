age = 20
status = "adult" if age >= 18 else "minor"
print(status)

n = -4
print("positive" if n > 0 else "zero" if n == 0 else "negative")  # chained

fee = 50 if age < 12 else 100
print("Ticket fee:", fee)
