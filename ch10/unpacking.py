def unpacking(name_age):
    if len(name_age) != 2:
        raise ValueError("Expected a tuple of two elements: (name, age)")
    name, age = name_age
    return f"Name: {name}, Age: {age}"


print(unpacking(("Felipe", 31)))
