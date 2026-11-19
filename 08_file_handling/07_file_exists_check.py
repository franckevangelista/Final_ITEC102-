import os

if os.path.exists("missing.txt"):
    print("File found")
else:
    print("missing.txt does not exist")

try:
    with open("missing.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Caught FileNotFoundError safely.")

# create-only mode: fails if it already exists
if os.path.exists("unique.txt"):
    os.remove("unique.txt")
with open("unique.txt", "x") as f:
    f.write("created once")
print("unique.txt created with mode x")
