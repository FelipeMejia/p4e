from collections import Counter

with open("sample.txt") as f:
    words = f.read().split()
    counts = Counter(words)
    t = list()
    for word, frequency in counts.items():
        t.append((frequency, word))

    t = list()
    for word, frequency in counts.items():
        t.append((frequency, word))
    t.sort(reverse=True)

    sorted_words = list()
    for frequency, word in t:
        sorted_words.append((word, frequency))

    print(sorted_words[:3])
