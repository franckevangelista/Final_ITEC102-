celsius = float(input("Temperature in Celsius: "))

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print(f"{'Celsius':>10}{'Fahrenheit':>14}{'Kelvin':>10}")
print("-" * 34)
print(f"{celsius:>10.1f}{fahrenheit:>14.1f}{kelvin:>10.2f}")

print("Rounded Fahrenheit:", round(fahrenheit))
