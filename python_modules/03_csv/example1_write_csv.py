import csv

rows = [
    ["name", "course", "score"],
    ["Ana", "BSIT", 92],
    ["Ben", "BSIT", 85],
    ["Cara", "BSCS", 78],
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("students.csv created")
