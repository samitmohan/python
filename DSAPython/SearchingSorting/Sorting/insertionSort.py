def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        nxt_element = arr[i]

        # Compare the current element with next one

        while (arr[j] > nxt_element) and (j >= 0):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = nxt_element


# you can add list of any numbers
list = [6, 5, 3, 1, 8, 7, 2, 4]
insertion_sort(list)
print(list)
