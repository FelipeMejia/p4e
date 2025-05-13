import string
from collections import Counter


def common_words(sentence):
    translator = str.maketrans("", "", string.punctuation)
    parsed_sentence = sentence.translate(translator).lower()
    words = parsed_sentence.split()
    counts = Counter(words)
    return [item for item, count in list(counts.most_common(3))]


text = "Hello, hello! Are you there? Yes, you!"
print(common_words(text))
