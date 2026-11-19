secret = 73
low, high = 1, 100
attempts = 0

while low <= high:
    guess = (low + high) // 2
    attempts += 1
    print(f"Attempt {attempts}: guess {guess}", end=" -> ")

    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("too low")
        low = guess + 1
    else:
        print("too high")
        high = guess - 1

print(f"Found {secret} in {attempts} attempts.")
