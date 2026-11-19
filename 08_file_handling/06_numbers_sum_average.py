with open("numbers.txt", "w") as f:
    for n in (85, 90, 78, 92, 88):
        f.write(str(n) + "\n")

total = 0
count = 0
with open("numbers.txt") as f:
    for line in f:
        total += int(line)
        count += 1

print("Total:", total)
print("Average:", total / count)
