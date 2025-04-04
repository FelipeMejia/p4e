try:
    temperature = float(input("Enter temperature in Celsius: "))
    fahrenheit = temperature * (9 / 5) + 32
    print(f"Fahrenheit: {fahrenheit:.1f}")
except ValueError:
    print("Numbers only, rookie")
