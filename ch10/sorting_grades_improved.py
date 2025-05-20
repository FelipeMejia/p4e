def sorting_grades(grades):
    return sorted(grades, key=lambda x: x[1], reverse=True)


students = [("Luis", 88), ("Ana", 92), ("Carlos", 85)]
print(sorting_grades(students))
