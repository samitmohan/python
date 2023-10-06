# https://leetcode.com/problems/rotate-function/
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        summ = 0
        F = 0
        for i in range(len(nums)):
            summ += nums[i]
            F += i * nums[i]  # calc function (index * number[index])

        global_sum = F  # for now
        # start from end and apply formula for pattern
        for i in range(len(nums) - 1, -1, -1):
            # f(k) = f(k - 1) + sum - length * last element
            F = F + summ - len(nums) * nums[i]
            global_sum = max(F, global_sum)
        return global_sum
