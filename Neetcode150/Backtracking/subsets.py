# https://leetcode.com/problems/subsets/description/
"""
from my understanding we should append a copy of subset array because array is passed as an reference and it will
always be modified later in other backtracking calls. so we need to append an instance of the modified subset
otherwise in the end it will just return an empty nested list. Since subset is an object and which is being
manipulated throughout the recursion, if I just add subset and on add or remove, object inside results will also
get changed since it would be a reference inside the results.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def generate(i):
            if i >= len(nums):  # base case
                # returns copy, does not modify original list
                ans.append(subset.copy())
                return
            # recursive (include ith element or don't)
            subset.append(nums[i])
            generate(i + 1)
            # pop
            subset.pop()

            # do not include ith element
            generate(i + 1)

        generate(0)
        return ans
