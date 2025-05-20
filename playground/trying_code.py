grades = [("Luis", 88), ("Ana", 92), ("Carlos", 85)]
grades.sort(reverse=True, key=lambda x: x[1])
print(grades)


def sort_by_value(d):
    t = list(d.items())
    t.sort(reverse=True, key=lambda x: x[1])
    print(t)


d = {"apple": 5, "banana": 3, "orange": 4}
sort_by_value(d)
