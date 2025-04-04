try:
    # Get hours worked and hourly rate from user
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    # Calculate gross pay
    payment = hours * rate
    print(f"Pay: ${payment:.2f}")
except ValueError as e:
    print("Enter a valid value", e)
