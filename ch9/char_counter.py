from collections import Counter


def char_counter(word):
    counts = Counter(word)
    return dict(counts.most_common(3))


print(char_counter("abracadabra"))
