def convert_and_divide(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return "Please use numbers only."
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except TypeError:
        return "Wrong data type."

print(convert_and_divide("10", "2"))
print(convert_and_divide("ten", "2"))
print(convert_and_divide("10", "0"))
print(convert_and_divide(None, "2"))
