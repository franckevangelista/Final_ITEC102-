text = "abc"
try:
    number = int(text)
    print("Number:", number)
except ValueError:
    print(f'"{text}" is not a valid integer.')
