with open("poem.txt", "w") as f:
    f.write("Roses are red\nViolets are blue\nPython is fun\nAnd so are you\n")

with open("poem.txt") as f:
    for number, line in enumerate(f, start=1):
        print(f"{number}: {line.strip()}")
