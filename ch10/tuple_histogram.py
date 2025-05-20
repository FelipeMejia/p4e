from collections import Counter


def word_histogram(words):
    counts = Counter(words)
    t = [(frequency, word) for word, frequency in counts.items()]
    t.sort(reverse=True)
    for frequency, word in t:
        print(f"{word}: {'#' * frequency}")


words = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple",
    "kiwi",
    "banana",
    "kiwi",
    "orange",
    "apple",
    "kiwi",
    "grape",
    "grape",
    "banana",
    "apple",
]
word_histogram(words)
