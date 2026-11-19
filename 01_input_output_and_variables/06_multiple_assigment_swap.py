a, b, c = 1, 2, 3
x = y = z = 0                 # same value for all three
print(a, b, c, x, y, z)

first = "left"
second = "right"
print("Before:", first, second)
first, second = second, first          # Python swap
print("After: ", first, second)

# the classic way with a temporary variable
m, n = 10, 20
temp = m
m = n
n = temp
print(m, n)
