# continue: skip multiples of 3
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# break: stop at the first number divisible by 7 after 20
n = 21
while True:
    if n % 7 == 0:
        print("First multiple of 7 above 20:", n)
        break
    n += 1
