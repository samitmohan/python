# https://leetcode.com/problems/kth-largest-element-in-an-array/
# create max heap and fill with array numbers
# keep removing element until kth element is reached
# return kth max element.
import heapq


# Sort : nums.sort() return nums[k - 1]
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * x for x in nums]
        heapq.heapify(nums)
        for i in range(k - 1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)
