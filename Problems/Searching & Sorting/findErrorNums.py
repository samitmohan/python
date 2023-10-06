# https://leetcode.com/problems/set-mismatch/description/
# Hint : You have a set of integers s, which originally contains all the numbers from 1 to n.
# [1, N] given : Cyclic Sort
# Error : 1 number got deleted and 1 number got repeated.
# you have to tell which number got repeated and deleted.

"""
0 1 2 3
1 2 2 4

0 1 2 3
1 2 2 4

2 is at the wrong index. : 2 is the repeated number
index + 1 is deleted number : 3
"""


class Solution:
    def findErrorNums(self, arr: List[int]) -> List[int]:
        i = 0
        while i < len(arr):
            correct_index = arr[i] - 1
            if arr[i] != arr[correct_index]:
                arr[i], arr[correct_index] = arr[correct_index], arr[i]
            else:
                i += 1
        # arr is sorted now, check for incorrect indexes
        for i in range(len(arr)):
            if arr[i] != i + 1:  # incorrect index (i + 1)
                return [arr[i], i + 1]
        return [-1, -1]
