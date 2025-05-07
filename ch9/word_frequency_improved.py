from collections import Counter

with open("romeo.txt") as f:
    words = f.read().split()

    counts = Counter(words)

print(counts.most_common(5))
