# https://leetcode.com/problems/minimum-average-difference
# Input: nums = [2,5,3,9,5,3]
# 2 and [5,3,9,5,3] -> 2/1 (i + 1) = 2 and 5 + 3 + 9 + 5 + 3 / 5 (n - i - 1) -> 5 so minimum (2,5) -> 2
# do this for every number and return index of min absolute difference
# Output: 3
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        # sum and curr sum and compare and find average
        sum = 0
        currSum = 0
        n = len(nums)
        for i in nums:
            sum += i  # 27

        min = 1e9  # current minimum
        ans = 0

        for i in range(0, n):
            currSum += nums[i]  # 2
            avg1 = currSum // (i + 1)  # 2 / 1 = 2
            # what if n - i - 1 = 0, then denom = 0, error : to fix add edge case
            if i == n - 1:
                # if avg already min
                if avg1 < min:
                    return n - 1  # ans
                else:
                    break
            avg2 = (sum - currSum) // (n - i - 1)  # 27 - 2 / 6 - 0 - 1 -> 5

            # finding answer
            if abs(avg1 - avg2) < min:
                # update min
                min = abs(avg1 - avg2)
                ans = i  # index of answer

        return ans
