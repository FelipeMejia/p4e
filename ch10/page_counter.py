def page_counter(logs):
    counts = dict()
    for _, page in logs:
        counts[page] = counts.get(page, 0) + 1

    visits = list(counts.items())
    visits.sort(reverse=True, key=lambda x: x[1])
    return visits


logs = [
    ("u1", "home"),
    ("u2", "about"),
    ("u1", "products"),
    ("u2", "home"),
    ("u3", "home"),
    ("u1", "about"),
    ("u2", "products"),
    ("u3", "products"),
    ("u2", "about"),
    ("u1", "home"),
]

print(page_counter(logs))
