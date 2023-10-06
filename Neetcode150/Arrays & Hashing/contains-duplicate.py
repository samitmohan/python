# https://leetcode.com/problems/contains-duplicate/

# Input: nums = [1,2,3,1]
# Output: true


class Solution(object):
    def containsDuplicate(self, nums):
        # approach -> hashset and insert elements in it and check
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False  # otherwise
