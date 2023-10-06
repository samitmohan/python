# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""
Base Case : index out of bound digit string
index >= digit.length()

Time : Combinations we have, output for n : 4^n (s : 9999)
O(n * 4^n)
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        # currentString : string we're building (empty initially)
        def helper(i, currentString):
            if i >= len(digits):  # base case
                ans.append(currentString)
                return
            for char in digit_to_char[digits[i]]:
                helper(i + 1, currentString + char)

        # non empty : if digits was empty : we end up returning [""] but in problem they want []
        if digits:
            helper(0, "")
        return ans
