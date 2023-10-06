# https://leetcode.com/problems/longest-subsequence-with-limited-sum/submissions/865631950/
from bisect import bisect_right
from itertools import accumulate


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = list(accumulate(nums))  # [4,5,2,1] -> [1,2,4,5] -> [1,3,7,12]
        ans = []
        for q in queries:
            maxseq = bisect_right(prefix_sum, q)  # binary search
            ans.append(maxseq)
        return ans
