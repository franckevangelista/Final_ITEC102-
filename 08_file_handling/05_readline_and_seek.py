with open("lines.txt", "w") as f:
    f.write("alpha\nbeta\ngamma\n")

with open("lines.txt") as f:
    print(f.readline().strip())      # alpha
    print(f.readline().strip())      # beta
    f.seek(0)                        # back to the beginning
    print(f.readline().strip())      # alpha again
    print("Position:", f.tell())
