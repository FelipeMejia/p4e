try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print(f"Sum: {x + y}")
    print(f"Difference: {x - y}")
    print(f"Product: {x * y}")
    if y != 0:
        print(f"Quotient: {x / y:.1f}")  #  decimal point
    else:
        print("Can't divide by zero, genius")
except ValueError:
    print("Numbers only, genius")
