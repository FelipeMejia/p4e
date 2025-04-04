def reverse_slice(lst, start, end):
    try:
        result = lst.copy()
        left, right = start, end
        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
        return result
    except IndexError:
        raise ValueError("Invalid Indices")


def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:  # Look up in sets is O(1)
            seen.add(item)
            result.append(item)
    return result


def flatten(lst):
    try:
        flattened = list()
        for sublist in lst:
            flattened.extend(sublist)
        return flattened
    except TypeError:
        raise TypeError("Please provide a list of lists")


def odd_indices(lst):
    return lst[1::2]


def cumulative_sum(lst):
    result = []
    total = 0
    for num in lst:
        total += num
        result.append(total)
    return result


def word_lengths(sentence):
    lengths = [
        len(item) for item in sentence.split()
    ]  # split with no argument handles better white spaces
    return lengths


def rotate_list(lst, n):
    if not lst:
        return []
    n = n % len(lst)
    return lst[-n:] + lst[:-n]


def insert_sorted(lst, num):
    lst.append(num)
    lst.sort()


def intersection(lst1, lst2):
    set1 = set(lst1)
    result = []
    seen = set()
    for item in lst2:
        if item in set1 and item not in seen:
            seen.add(item)
            result.append(item)
    return result


def chunk_list(lst, size):
    if size <= 0:
        return []
    i = 0
    result = []
    while i < len(lst):
        result.append(lst[i : i + size])
        i += size
    return result


print("Reverse slice")
try:
    print(reverse_slice([1, 2, 3, 4, 5], 1, 3))
    print(reverse_slice([1, 2, 3, 4, 5, 6, 7, 8], 5, 6))
    print(reverse_slice([1, 2, 3, 4, 5], 3, 3))
    print(reverse_slice([1, 2, 3, 4, 5], -1, 0))
    print(reverse_slice([1, 2, 3, 4, 5], 1, 5))
except ValueError as e:
    print(e)


print("Remove duplicates")
print(remove_duplicates([1, 2, 2, 3, 1, 4]))
print(remove_duplicates([1, 1, 1, 1, 1, 1]))
print(
    remove_duplicates(
        [
            1,
            2,
            2,
            3,
            1,
            4,
            4,
            5,
            6,
            6,
            7,
            1,
            8,
            2,
        ]
    )
)
print(remove_duplicates([1, 1, 1, 1, 1, 1, "a", "a"]))

try:
    print("\nFlatten lists")
    print(flatten([[1, 2], [3, 4], [5]]))
    print(flatten([[1, 2], [4], [5]]))
    print(flatten([]))
    print(flatten([[], [1]]))
except TypeError as e:
    print(e)

print("\n Odd indices")
print(odd_indices([10, 20, 30, 40, 50]))
print(odd_indices([10]))
print(odd_indices([]))

print("\nCumulative sume")
print(cumulative_sum([1, 2, 3, 4]))
print(cumulative_sum([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, +100]))
print(
    cumulative_sum(
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, +100, 1, 2, 3, -25, 6]
    )
)
print(cumulative_sum([0, 0, 0]))
print(cumulative_sum([-1, -2, -3]))

print("\nWord lengths")
print(word_lengths("I am learning Python"))
print(word_lengths("Hola como estás, hace tiempo no se de ti."))
print(word_lengths("I am     here"))
print(word_lengths(""))
print(word_lengths("  "))

print("\nRotate list")
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 10))
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([], 3))

print("\nInsert sorted")
lst = [1, 3, 5]
insert_sorted(lst, 4)
print(lst)
insert_sorted(lst, -2)
print(lst)

lst2 = []
insert_sorted(lst2, 1)
print(lst2)

lst3 = [1, 2]
insert_sorted(lst3, 2)
print(lst3)

print("\nIntersection:")
print(intersection([1, 2, 3, 2], [2, 3, 4]))
print(intersection([1, 2, 3, 2], [5, 6, 7]))
print(
    intersection(
        [1, 2, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        [5, 6, 7, 16, 17, 18, 19, 20, 21],
    )
)
print(intersection([], []))

print("\nChunk list: ")
print(chunk_list([1, 2, 3, 4, 5], 2))
print(chunk_list([1, 2, 3, 4, 5], 3))
print(chunk_list([1, 2, 3, 4, 5], 0))
print(chunk_list([1, 2, 3, 4, 5], -1))
print(chunk_list([], -1))
