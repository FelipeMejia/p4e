from collections import Counter


def duplicates(lst):
    counts = Counter(lst)
    duplicates = list()
    for key in counts:
        times = counts.get(key)
        if times >= 2:
            duplicates.append(key)

    return duplicates


result = duplicates(["x", "y", "x", "z", "y", "y"])
print(result)
