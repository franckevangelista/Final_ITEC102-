for number in range(2, 51):
    is_prime = True
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break                # no need to keep checking
    if is_prime:
        print(number, end=" ")
print()
