import csv

with open("students.csv", "w", newline="") as f:
    csv.writer(f).writerows([["name", "course", "score"], ["Ana", "BSIT", 92], ["Ben", "BSIT", 85], ["Cara", "BSCS", 78]])

passers = []
with open("students.csv", newline="") as f:
    for row in csv.DictReader(f):
        if int(row["score"]) >= 80:
            passers.append(row)
            print(f"{row['name']} ({row['course']}) passed with {row['score']}")

with open("passers.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "course", "score"])
    writer.writeheader()
    writer.writerows(passers)
print("passers.csv written")