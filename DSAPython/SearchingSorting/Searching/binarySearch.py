def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [1, 2, 3, 4, 5, 7]
target_value = 5
result_index = binary_search(arr, target_value)
print(result_index)  # Output: 4


# An Order Agnostic Binary Search Algorithm is used when the order of the elements in a sorted array is not known.
def order_agnostic_binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    is_ascending = arr[left] < arr[right]
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if is_ascending:
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if arr[mid] < target:
                right = mid - 1
            else:
                left = mid + 1
    return -1


arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [6, 5, 4, 3, 2, 1]
target_value = 4
result_index1 = order_agnostic_binary_search(arr1, target_value)
result_index2 = order_agnostic_binary_search(arr2, target_value)
print(result_index1)  # Output: 3
print(result_index2)  # Output: 2
