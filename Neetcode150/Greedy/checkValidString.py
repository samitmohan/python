# https://leetcode.com/problems/valid-parenthesis-string/
# https://leetcode.com/problems/valid-parenthesis-string/solutions/107570/java-c-python-one-pass-count-the-open-parenthesis/
# https://www.youtube.com/watch?v=QhPdNS143Qg (Revisit)

"""
* : wildcard : can mean (, _, )
Time : O(n) (trick)

()
left open parenthesis : 0 -> 1 -> 0 (when right parenthesis seen)
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0
        for c in s:
            if c == "(":
                left_min, left_max = left_min + 1, left_max + 1
            elif c == ")":
                left_min, left_max = left_min - 1, left_max - 1
            else:  # wildcard
                left_min, left_max = left_min - 1, left_max + 1

            # complicated part : dry run : (*) (
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0
        return left_min == 0
