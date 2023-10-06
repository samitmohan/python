# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
# Cyclic Sort same as find duplicates
class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        i = 0
        while i < len(arr):
            correct_index = arr[i] - 1
            if arr[i] != arr[correct_index]:
                arr[i], arr[correct_index] = arr[correct_index], arr[i]
            else:
                i += 1
        # find incorrect index
        ans = []
        for i in range(len(arr)):
            if arr[i] != i + 1:
                ans.append(arr[i])
        return ans
