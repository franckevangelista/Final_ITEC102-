rows = 5

print("Right triangle")
for r in range(1, rows + 1):
    for c in range(r):
        print("*", end="")
    print()

print("\nPyramid")
for r in range(1, rows + 1):
    print(" " * (rows - r) + "*" * (2 * r - 1))
