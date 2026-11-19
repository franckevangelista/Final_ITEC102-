while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            print("Age must be positive.")
            continue
        break                    # valid input, leave the loop
    except ValueError:
        print("That is not a number. Try again.")

print("Your age is", age)
