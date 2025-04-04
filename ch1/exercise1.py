name = input("Enter your name: ")
if not name.strip():
    print("No name entered, using 'Stranger'.")
    name = "Stranger"

print(f"Hello {name}! You're stuck with me now.")
