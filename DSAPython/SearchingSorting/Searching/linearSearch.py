def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [4, 2, 1, 5, 7, 3]
target_value = 5
result_index = linear_search(arr, target_value)
print(result_index)  # Output: 3
