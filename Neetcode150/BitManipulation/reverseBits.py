# https://leetcode.com/problems/reverse-bits/description/
"""
https://www.youtube.com/watch?v=UcoN6UjAI64
Time & Space : O(1)
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            bit = (n >> i) & 1
            ans = ans | (bit << (31 - i))
        return ans
