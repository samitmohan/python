# https://leetcode.com/problems/number-of-1-bits/description/
"""
Mod + Right Shift
1011 % 2 = if lastDigit = 1 -> increment ans
Shift to right 1011 >> 1 : 101 and do the same -> increment ans
101 >> 1 : 10 % 2 != 1, so ignore and right shift : 1 -> increment ans
return ans = 3
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n % 2
            n = n >> 1
        return ans
