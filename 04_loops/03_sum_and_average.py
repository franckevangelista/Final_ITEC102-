n = 100
total = 0
for number in range(1, n + 1):
    total += number

print(f"Sum of 1 to {n} = {total}")
print(f"Average = {total / n}")
print("Check with formula:", n * (n + 1) // 2)
