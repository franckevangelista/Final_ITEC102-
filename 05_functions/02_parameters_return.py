def add(a, b):
    return a + b

def area_of_rectangle(length, width):
    return length * width

result = add(5, 7)
print("5 + 7 =", result)
print("Area:", area_of_rectangle(4, 6))
print(add(add(1, 2), add(3, 4)))   # functions can be nested in calls
