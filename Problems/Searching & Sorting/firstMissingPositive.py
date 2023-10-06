# Cyclic sort example
# https://leetcode.com/problems/first-missing-positive/description/

"""
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Note : ignore -ve
"""


class Solution:
    def firstMissingPositive(self, arr: List[int]) -> int:
        # start looking from i, swap with correct index, only move i pointer when i is at correct index.
        i = 0
        while i < len(arr):
            correct_index = arr[i] - 1  # index = value - 1
            # edge case added (case 2) and ignore negatives also
            if 0 < arr[i] <= len(arr) and arr[i] != arr[correct_index]:
                arr[i], arr[correct_index] = arr[correct_index], arr[i]
            else:
                i += 1
        # search for first missing number

        for i in range(len(arr)):
            if arr[i] != i + 1:
                return i + 1

        return len(arr) + 1  # case 2 [3, 4, 2, 1] : 1, 2, 3, 4 : answer = 5
