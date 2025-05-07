def count_letters(text):
    count = dict()
    for char in text:
        count[char] = count.get(char, 0) + 1
    return count


print(count_letters("banana"))
