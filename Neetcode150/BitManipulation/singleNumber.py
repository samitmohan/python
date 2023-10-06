# https://leetcode.com/problems/single-number/
"""
XOR gate ; same values : 0 different values : 1
00 : 0
01 : 1
10 : 1
11 : 0

nums = [2, 2, 1]
unique = 0
2 ^ unique : 2 xor 0 : 10 XOR 0 : 10 = 2

"""


# Easy Hashmap Solution : O(N) space
class Solution:
    def singleNumber(nums):
        hm = {}
        for x in nums:
            if x in hm:
                hm[x] += 1
            else:
                hm[x] = 1
        for k, v in hm.items():
            if v == 1:
                return k


# XOR Solution : Same numbers will have 0 as XOR computation (2,2,1,1) : 0 but different numbers (unique) will have
# answer : (2,2,1) : (2 ^ 2 : 0, 2 ^ 1 : 1) answer : 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for number in nums:
            ans = ans ^ number
        return ans


if __name__ == "__main__":
    nums = [2, 2, 1]
    print(Solution.singleNumber(nums))
