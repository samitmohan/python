# https://leetcode.com/problems/maximum-ice-cream-bars/
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans = 0
        costs.sort()  # [1,1,2,3,4] O(nlogn)
        for price in costs:
            if price <= coins:
                ans += 1
                coins -= price
            else:
                break
        return ans
