# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i, target, temp, ans):
            if i == len(candidates):
                if target == 0 and temp not in ans:
                    ans.append(temp.copy())
                return
            if candidates[i] <= target:
                # include element
                temp.append(candidates[i])
                helper(i, target - candidates[i], temp, ans)
                temp.pop()  # backtrack
            # do not include element
            helper(i + 1, target, temp, ans)
            return ans

        temp, ans = [], []
        return helper(0, target, temp, ans)
