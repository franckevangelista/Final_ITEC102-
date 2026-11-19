choice = 3

match choice:
    case 1:
        print("Order: Burger")
    case 2:
        print("Order: Pizza")
    case 3:
        print("Order: Pasta")
    case _:                      # default case
        print("Invalid choice")

day = "sat"
match day:
    case "sat" | "sun":          # multiple patterns
        print("Weekend")
    case _:
        print("Weekday")
