# Week 1 Problem Set

1. **Reverse Slice**: Write a function `reverse_slice(lst, start, end)` that takes a list and two indices, then returns a new list with the slice from `start` to `end` (inclusive) reversed, leaving the original list unchanged. Example: `reverse_slice([1, 2, 3, 4, 5], 1, 3)` → `[1, 4, 3, 2, 5]`.

2. **Duplicate Remover**: Write a function `remove_duplicates(lst)` that removes all duplicate elements from a list and returns the modified list, keeping the first occurrence of each element. Example: `remove_duplicates([1, 2, 2, 3, 1, 4])` → `[1, 2, 3, 4]`.

3. **List Flattener**: Write a function `flatten(lst)` that takes a list of lists and returns a single list with all elements flattened. Example: `flatten([[1, 2], [3, 4], [5]])` → `[1, 2, 3, 4, 5]`.

4. **Odd Indices**: Write a function `odd_indices(lst)` that returns a new list containing elements at odd indices (1, 3, 5, etc.) from the input list. Example: `odd_indices([10, 20, 30, 40, 50])` → `[20, 40]`.

5. **Cumulative Sum**: Write a function `cumulative_sum(lst)` that takes a list of numbers and returns a new list where each element is the sum of all elements up to that point in the original list. Example: `cumulative_sum([1, 2, 3, 4])` → `[1, 3, 6, 10]`.

6. **Word Lengths**: Write a function `word_lengths(sentence)` that takes a string sentence, splits it into words, and returns a list of the lengths of each word. Example: `word_lengths("I am learning Python")` → `[1, 2, 8, 6]`.

7. **Rotate List**: Write a function `rotate_list(lst, n)` that rotates a list to the right by `n` positions. Example: `rotate_list([1, 2, 3, 4, 5], 2)` → `[4, 5, 1, 2, 3]`.

8. **Insert Sorted**: Write a function `insert_sorted(lst, num)` that takes a sorted list of numbers and inserts a new number into the correct position to keep the list sorted. Modify the original list. Example: `lst = [1, 3, 5]; insert_sorted(lst, 4)` → `lst = [1, 3, 4, 5]`.

9. **List Intersection**: Write a function `intersection(lst1, lst2)` that returns a new list containing only the elements present in both input lists, with no duplicates. Example: `intersection([1, 2, 3, 2], [2, 3, 4])` → `[2, 3]`.

10. **Chunk List**: Write a function `chunk_list(lst, size)` that splits a list into smaller lists of size `size`. If the last chunk is smaller, include it as is. Example: `chunk_list([1, 2, 3, 4, 5], 2)` → `[[1, 2], [3, 4], [5]]`.

# Week 2 Problem Set

# Coding Problem List

1. **Merge Sorted Lists**  
   Write `merge_sorted(lst1, lst2)` to merge two sorted lists into one sorted list.  
   **Example:** `[1, 3, 5], [2, 4, 6]` → `[1, 2, 3, 4, 5, 6]`.

2. **List Partition**  
   Write `partition(lst, pivot)` to split a list into two lists: elements `< pivot` and `≥ pivot`.  
   **Example:** `[3, 1, 4, 1, 5], 3` → `([1, 1], [3, 4, 5])`.

3. **Max Subarray Sum**  
   Write `max_subarray_sum(lst)` to find the maximum sum of a contiguous subarray.  
   **Example:** `[-2, 1, -3, 4, -1, 2, 1]` → `6` (subarray `[4, -1, 2, 1]`).

4. **Rotate Matrix**  
   Write `rotate_matrix(lst)` to rotate a 2D list (matrix) 90° clockwise.  
   **Example:** `[[1, 2], [3, 4]]` → `[[3, 1], [4, 2]]`.

5. **Common Elements**  
   Write `common_elements(lst1, lst2, lst3)` to find elements common to three lists.  
   **Example:** `[1, 2, 3], [2, 3, 4], [2, 3, 5]` → `[2, 3]`.

6. **List Compression**  
   Write `compress(lst)` to compress consecutive duplicates into a count and value pair.  
   **Example:** `[1, 1, 1, 2, 3, 3]` → `[[3, 1], [1, 2], [2, 3]]`.

7. **Longest Increasing Subsequence**  
   Write `lis(lst)` to find the length of the longest increasing subsequence.  
   **Example:** `[10, 9, 2, 5, 3, 7]` → `4` (subsequence `[2, 3, 7]`).

8. **Zigzag Traversal**  
   Write `zigzag(lst)` for a 2D list, returning elements in zigzag order.  
   **Example:** `[[1, 2, 3], [4, 5, 6]]` → `[1, 2, 3, 6, 5, 4]`.

9. **List Interleaving**  
   Write `interleave(lst1, lst2)` to interleave two lists.  
   **Example:** `[1, 2, 3], [4, 5, 6]` → `[1, 4, 2, 5, 3, 6]`.

10. **Circular Shift Check**  
    Write `is_circular_shift(lst1, lst2)` to check if one list is a circular shift of another.  
    **Example:** `[1, 2, 3], [3, 1, 2]` → `True`.
