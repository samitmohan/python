# https://leetcode.com/problems/k-closest-points-to-origin/description/
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            pts.append([dist, x, y])  # ([8, -2, -2], [10, 1, 3])
        ans = []
        # convert to heap (O(n))
        heapq.heapify(pts)
        # keep popping from points until k
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            ans.append([x, y])  # answer points (-2,-2)
        return ans
