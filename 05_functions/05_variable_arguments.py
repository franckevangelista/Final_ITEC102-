def total(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result

def biggest(*numbers):
    best = numbers[0]
    for n in numbers:
        if n > best:
            best = n
    return best

print(total(1, 2, 3))
print(total(10, 20, 30, 40, 50))
print(biggest(4, 99, 23, 7))
