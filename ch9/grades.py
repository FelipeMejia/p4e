def group_grades(grades):
    group = dict()
    for student, grade in grades:
        if student not in group:
            group[student] = []
        group[student].append(grade)
    return group


grades = [("Ana", 90), ("Luis", 85), ("Ana", 80), ("Luis", 88), ("Carlos", 95)]
print(group_grades(grades))
