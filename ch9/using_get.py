words = ["dog", "cat", "dog", "mouse", "cat", "dog"]
counts = dict()

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
