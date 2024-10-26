def divide_numbers(x, y):
    try:
        result = x / y
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))
divide_numbers(numerator, denominator)
