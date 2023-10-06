# https://leetcode.com/problems/edit-distance/description/
"""
if w1[i] = w2[j] : sub-problem : (i+1, j+1) (0 operations)
word1 = abc
word2 = abc
acd
b (i) and c(j) not equal : insert, delete, replace :
Insert : acbd : now no need to move i pointer, need to find b in word2
    operations = 1 (shift pointer) : (i, j + 1) : 1 operation
Delete : (i + 1, j) : abd : ad and acd remains same : 1 operation
Replace : from word1 that shows up in word2 : abd replace b with c : acd now word1 = word2 : (i + 1, j + 1) (same as equal) : 1 opeartion

Similar to LCS
Good explanation : https://www.youtube.com/watch?v=XYi2-LPrwm4
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]
