# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

# greedy + hashing
# tasks = [2,2,3,3,2,4,4,4,4,4]
class Solution:
    def minimumRounds(tasks):
        # hash map -> key (difficulty) val (occurences)
        hm = {}
        for i in tasks:
            if i in hm:
                hm[i] += 1  # val
            else:
                hm[i] = 1

        count = 0
        for i, val in hm.items():
            if val == 1:
                return -1
            if val % 3 == 0:
                count += val // 3
            else:
                count == (val // 3) + 1

        return count
