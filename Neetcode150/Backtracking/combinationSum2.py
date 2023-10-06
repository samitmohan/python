# https://leetcode.com/problems/combination-sum-ii/description/
"""
Unique combinations : no duplications
1,7 and 7,1 :: NO.
if (i == index || candidates[i] != candidates[i - 1])
Time : O(2^ns)
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def helper(index, currSum, target):
            if target < 0:
                return
            if target == 0:  # base case
                ans.append(currSum[:])
                return
            for i in range(index, len(candidates)):
                # skip duplicates
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                currSum.append(candidates[i])
                helper(i + 1, currSum, target - candidates[i])
                currSum.pop()

        helper(0, [], target)
        return ans
