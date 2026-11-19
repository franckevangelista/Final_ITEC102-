import csv

with open("students.csv", "w", newline="") as f:
    csv.writer(f).writerows([["name", "course", "score"], ["Ana", "BSIT", 92], ["Ben", "BSIT", 85], ["Cara", "BSCS", 78]])

total = 0
with open("students.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)                  # first row
    print("Columns:", header)
    for row in reader:
        print(row[0], "->", row[2])
        total += int(row[2])               # strings must be converted
print("Total score:", total)
