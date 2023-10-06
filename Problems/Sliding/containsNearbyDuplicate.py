# https://leetcode.com/problems/contains-duplicate-ii/submissions/897201098/
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # sliding window
        window = set()  # store answer
        left = 0
        for right in range(len(nums)):
            # window shift
            if left + right > k:
                # change our sliding window -> remove left pointer and increment left pointer by one
                window.remove(nums[left])
                left += 1
            if nums[right] in window:  # already present
                return True
            else:
                window.add(nums[right])
        return False  # otherwise
