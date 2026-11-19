with open("log.txt", "w") as f:
    f.write("First entry\n")

with open("log.txt", "a") as f:        # a = append
    f.write("Second entry\n")
    f.write("Third entry\n")

with open("log.txt") as f:
    print(f.read())
