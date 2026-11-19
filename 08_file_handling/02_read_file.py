with open("sample.txt", "w") as f:
    f.write("Hello file!\nThis is line 2.\n")

with open("sample.txt", "r") as f:
    content = f.read()

print(content)
print("Characters:", len(content))
