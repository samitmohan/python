# https://leetcode.com/problems/powx-n/description/
"""
Instead of O(N) : for loop and multiply n times : use D&C
2^10 : calculate 2^5 and just multiply with itself. Break this down more
2^5 : 2^2 * 2^2 * 2 (eliminate half the work)
2^2 : 2^1 * 2^1

Time : O(log(n))
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x ^ -n = 1 / x ^ n : take abs value to fix and return 1 / abs(val)
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            # n = 4, n = 2 (what if we had odd : n = 5, n = 2)
            # if it's odd -> need to multiply it 1 more time
            # x^5 = x^2 * x^2 * x
            ans = helper(x, n // 2)
            ans = ans * ans
            return x * ans if n % 2 else ans

        ans = helper(x, abs(n))
        return ans if n >= 0 else 1 / ans
