fhand = open("romeo.txt")
counts = dict()

for line in fhand:
    words = line.rstrip().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

most_common_frequencies = sorted(counts.items(), key=lambda item: item[1], reverse=True)
for word, count in most_common_frequencies[:5]:
    print(f"{word}: {count}")
