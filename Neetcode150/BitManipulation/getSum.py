# https://leetcode.com/problems/sum-of-two-integers/description/
"""
XOR numbers. 9 XOR 11 = 0010 (2)
1001 (9)
1011 (11)

carry places : 2
1010 : carry
1001
1011
Add carry to result XOR

a & b << 1 (shift to left for all ANDS)
1001
1011
----
1001

shift by 1
 0010
1001_

Keep doing XOR + AND
Time : O(1)
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        def add(a, b):
            if not a or not b:
                return a or b
            return add(a ^ b, (a & b) << 1)

        if a * b < 0:  # assume a < 0, b > 0
            if a > 0:
                return self.getSum(b, a)
            if add(~a, 1) == b:  # -a == b
                return 0
            if add(~a, 1) < b:  # -a < b
                return add(~add(add(~a, 1), add(~b, 1)), 1)  # -add(-a, -b)

        return add(a, b)  # a * b >= 0 or (-a) > b > 0
