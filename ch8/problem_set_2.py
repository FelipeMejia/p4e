def merge_sorted(lst1, lst2):
    i, j = 0, 0
    new_list = list()
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            new_list.append(lst1[i])
            i += 1
        else:
            new_list.append(lst2[j])
            j += 1

    new_list.extend(lst1[i:])
    new_list.extend(lst2[j:])
    return new_list


def partition(lst, pivot):
    lst1 = []
    lst2 = []
    for item in lst:
        if item < pivot:
            lst1.append(item)
        else:
            lst2.append(item)
    return (lst1, lst2)


def max_subarray_sum(lst):
    if not lst:
        return 0
    max_sum = current_sum = lst[0]
    for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


def rotate_matrix(lst):
    ans = []
    i = 0
    while i < len(lst[0]):
        j = len(lst) - 1
        row = []
        while j >= 0:
            row.append(lst[j][i])
            j -= 1
        ans.append(row)
        i += 1
    return ans


def common_elements(lst1, lst2, lst3):
    result = list()
    for item in lst1:
        if (item in lst2) and (item in lst3):
            result.append(item)

    return result


def compress(lst):
    occurrences = dict()
    answer = list()
    for item in lst:
        occurrences[item] = occurrences.get(item, 0) + 1
    for key in occurrences.keys():
        answer.append([occurrences[key], key])
    return answer


def lis(lst):
    end_of_list = len(lst) - 1
    greater_subsequence = 1
    for i in range(end_of_list):
        max = 1
        for j in range(i + 1, end_of_list):
            if lst[j] > lst[i]:
                max = len(lst[i : j + 1])
        if max > greater_subsequence:
            greater_subsequence = max
    return greater_subsequence


print("Merge sorted:")
print(merge_sorted([1, 3, 5], [2, 4, 6]))
print(merge_sorted([], []))
print(merge_sorted([-58, -9, 0], [-100, 1, 2]))
print(merge_sorted([1, 2], [3, 4, 5, 6]))

print("\nPartition:")
print(partition([3, 1, 4, 1, 5], 3))
print(partition([3, 1, 4, 1, 5], 0))
print(partition([], 100))
print(partition([3, 1, 4, 1, 5], 6))

print("\nMax Subarray Sum:")
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1]))
print(max_subarray_sum([1]))
print(max_subarray_sum([1, 1]))
print(max_subarray_sum([6, -4]))
print(max_subarray_sum([]))
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1]))

print("\nRotate matrix:")
print(rotate_matrix([[1, 2], [3, 4]]))
print(rotate_matrix([[1, 2, 3], [4, 5, 6]]))

print("\nCommon Elements:")
print(common_elements([1, 2, 3], [2, 3, 4], [2, 3, 5]))
print(common_elements([], [2, 3, 4], [2, 3, 5]))

print("\nList compression:")
print(compress([1, 1, 1, 2, 3, 3]))

print("\nLongest Increasing Subsequence")
print(lis([10, 9, 2, 5, 3, 7]))
