# https://leetcode.com/problems/find-peak-element/description/
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # modified binary search
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            # left side bigger (check for out of bounds condition) : look on left side
            if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                low = mid + 1
            # right side bigger
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                high = mid - 1
            else:
                return mid  # answer
