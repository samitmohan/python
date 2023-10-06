# https://leetcode.com/problems/subsets-ii/
"""
Same as subsets but with no duplicates : keep a boolean prev_seen variable
if current val = prevs val -> duplicate
also make sure i is in within boundries.
and if prevs value is ignored = this value should be ignored also
    if (i > 0 && nums[i] == nums[i - 1] && (!prevs)) return;

Time : O(2^n)
"""


# Since we're sorting array : duplicates will be right next to each other


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        nums.sort()

        def generate(i, prev_seen):
            if i >= len(nums):
                ans.append(subset.copy())
                return
            # recursive
            # do not include
            generate(i + 1, False)
            # no duplicates (why i > 0?)
            if i > 0 and not prev_seen and nums[i] == nums[i - 1]:
                return
            # include
            subset.append(nums[i])
            generate(i + 1, True)
            subset.pop()

        generate(0, False)
        return ans
