# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
# Cyclic sort.

# if range = [0, N] : every element will be at index = value
# if range = [1, N] : every element will be at index = value - 1
# answer : incorrect indexes
def findDisappearedNumbers(arr):
    i = 0
    while i < len(arr):
        correct_index = arr[i] - 1
        if arr[i] != arr[correct_index]:
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            i += 1
    # arr is sorted now, check for incorrect indexes
    ans = []
    for i in range(len(arr)):
        if arr[i] != i + 1:  # incorrect index (i + 1)
            ans.append(i + 1)
    return ans


if __name__ == "__main__":
    arr = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDisappearedNumbers(arr))
