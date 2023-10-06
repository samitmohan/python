# https://leetcode.com/problems/partition-labels/

"""
Hashmap : char : lastIndex it occurs at
size (initially 0 (window size)) and end (denoting end index of char)
Time : O(n) and Space : O(1)
"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i  # char to index mapping

        ans = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            # update end if lastIndex value > end found
            end = max(end, last_index[c])
            if i == end:  # last reached
                ans.append(size)
                size = 0  # set back to 0
        return ans
