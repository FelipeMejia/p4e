try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))

    if hours < 0 or rate < 0:
        print("Hours and rate can't be negative, idiot")
        exit()

    if hours > 40:
        total_pay = (40 * rate) + (hours - 40) * (1.5 * rate)
    else:
        total_pay = hours * rate

    print(f"Pay: {total_pay:.2f}")
except ValueError:
    print("Numbers only, idiot")
