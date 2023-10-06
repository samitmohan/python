# https://leetcode.com/problems/greatest-common-divisor-of-strings/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        def is_divisible(length):
            if len1 % length or len2 % length:
                return False  # if it can't divide it completely (% != 0)
            # else it divides completely, how many times we need to divide in order to get ans
            factor1 = len1 // length
            factor2 = len2 // length
            return str1[:length] * factor1 == str1 and str1[:length] * factor2 == str2

        for length in range(min(len1, len2), 0, -1):  # greedy approach
            if is_divisible(length):
                return str1[:length]
        # else empty
        return ""
