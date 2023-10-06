# https://leetcode.com/problems/largest-number/description/
class Solution:
    # 9, 34 : 934 > 349
    # Convert to strings -> append -> compare strings

    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1  # n1 goes first
            else:
                return 1  # n2 goes first

        nums = sorted(nums, key=cmp_to_key(compare))

        # [0,0,0,1] = 1000 || [0,0,0] = "000" no -> "0" : convert to int and back to string

        return str(int("".join(nums)))
