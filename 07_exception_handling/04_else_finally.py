def safe_sqrt(value):
    try:
        number = float(value)
        if number < 0:
            raise ValueError("negative number")
    except ValueError as error:
        print("Error:", error)
    else:
        print("Square root:", number ** 0.5)
    finally:
        print("Done processing", repr(value))
        print("-" * 25)

safe_sqrt("49")
safe_sqrt("-4")
safe_sqrt("hello")
