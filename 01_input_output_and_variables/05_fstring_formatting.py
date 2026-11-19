item = "Laptop"
price = 45999.5
qty = 3

print(f"Item: {item}")
print(f"Price: PHP {price:,.2f}")            # 45,999.50
print(f"Total: PHP {price * qty:,.2f}")
print(f"[{item:<10}]")                       # left align
print(f"[{item:>10}]")                       # right align
print(f"[{item:^10}]")                       # center
print(f"Discount: {0.15:.0%}")               # 15%
