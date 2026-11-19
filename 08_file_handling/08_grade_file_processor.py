with open("grades.txt", "w") as f:
    f.write("Ana,92\nBen,85\nCara,78\nDan,95\nEve,88\n")

total = 0
count = 0
best_name = ""
best_score = -1

with open("grades.txt") as f:
    for line in f:
        name, score = line.strip().split(",")
        score = int(score)
        total += score
        count += 1
        if score > best_score:
            best_score = score
            best_name = name

with open("report.txt", "w") as out:
    out.write(f"Students: {count}\n")
    out.write(f"Average: {total / count:.2f}\n")
    out.write(f"Top student: {best_name} ({best_score})\n")

with open("report.txt") as out:
    print(out.read())
