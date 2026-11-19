CORRECT_PIN = 4321
MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    try:
        pin = int(input(f"Enter PIN ({MAX_ATTEMPTS - attempts} tries left): "))
    except ValueError:
        print("PIN must be digits only.")
        attempts += 1
        continue

    if pin == CORRECT_PIN:
        print("Access granted.")
        break
    attempts += 1
    print("Wrong PIN.")
else:
    # the loop's else runs only if break was never reached
    print("Account locked.")
