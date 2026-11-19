a, b, c = 5, 5, 8

# Triangle inequality: each side must be shorter than the sum of the other two
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        kind = "equilateral"
    elif a == b or b == c or a == c:
        kind = "isosceles"
    else:
        kind = "scalene"

    # right-triangle check
    sides = sorted([a, b, c])
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        kind += " (and right-angled)"
    print(f"Sides {a}, {b}, {c}: {kind} triangle")
else:
    print("These sides cannot form a triangle.")
