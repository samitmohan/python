# https://leetcode.com/problems/longest-consecutive-sequence/

# Input: nums = [100,4,200,1,3,2]
# Output: 4

class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        # TC -> O(N) single pass
        s = set(arr)  # 100, 4, 200, 1, 3, 2
        answer = 0
        for number in s:
            if (number - 1) not in s:  # if no match then answer 1
                length = 1  # min
                while (number + length in s):  # if 101 present -> length++, 102 present -> length++
                    length += 1
                answer = max(length, answer)  # update (worst case -> 1, 0 -> ans = 1)
        return answer
