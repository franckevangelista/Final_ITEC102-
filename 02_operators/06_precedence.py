print(2 + 3 * 4)            # 14, multiplication first
print((2 + 3) * 4)          # 20
print(2 ** 3 ** 2)          # 512, ** goes right to left
print(10 - 4 - 3)           # 3, left to right
print(not True or True)     # True, not before or
print(True or False and False)  # True, and before or

# average: parentheses are REQUIRED
a, b, c = 80, 90, 100
print("Wrong:", a + b + c / 3)
print("Right:", (a + b + c) / 3)
