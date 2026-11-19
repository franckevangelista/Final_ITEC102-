item = input("Item name: ")
price = float(input("Price per piece: "))
qty = int(input("Quantity: "))

subtotal = price * qty
vat = subtotal * 0.12
total = subtotal + vat

print("\n" + "=" * 30)
print(f"{'RECEIPT':^30}")
print("=" * 30)
print(f"{item} x{qty}")
print(f"{'Subtotal:':<15}{subtotal:>13,.2f}")
print(f"{'VAT (12%):':<15}{vat:>13,.2f}")
print(f"{'TOTAL:':<15}{total:>13,.2f}")
print("=" * 30)
