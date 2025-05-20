def sorting_grades(grades):
    t = list()
    for student, grade in grades:
        t.append((grade, student))

    t.sort(reverse=True)

    result = list()
    for grade, student in t:
        result.append((student, grade))

    return result


students = [("Luis", 88), ("Ana", 92), ("Carlos", 85)]
print(sorting_grades(students))
