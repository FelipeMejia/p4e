from collections import Counter

with open("sample.txt") as f:
    words = f.read().split()
    bigrams = list()
    for i in range(len(words) - 1):
        bigrams.append(f"{words[i]} {words[i+1]}")

    counts = Counter(bigrams)
    print(counts.most_common(5))
