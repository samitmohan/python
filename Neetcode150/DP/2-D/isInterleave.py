# https://leetcode.com/problems/interleaving-string/description/
"""
Observations:
    (len) Total characters in both strings need to match total characters in final string.
    if s3 starts with a then obviously s1 or s2 should start with a

s1 = aabcc
s2 = dbbca
s3 = aadbbcbcac

pointers i1, i2, i3
i1 + i2 = i3 (index)
Start with (0,0)

Answer : True / False
if we find single True : return True (no need of caching)
2D array with right side empty. (LCS) (Extra Layer)
Base case : both pointers in both strings out of bound.

T : O(m * n)
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        # k = i + j
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]

            # caching
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            dp[(i, j)] = False  # neither of them return True : cache False

            return False  # otherwise

        return dfs(0, 0)
