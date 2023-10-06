# https://leetcode.com/problems/roman-to-integer/submissions/879687255/
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        mp = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(0, len(s) - 1):
            if mp[s[i]] < mp[s[i + 1]]:
                ans -= mp[s[i]]
            else:
                ans += mp[s[i]]

        # the trick is that the last letter is always added bcs it has nothing to compare to in front of it.
        return ans + mp[s[-1]]
