# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        maxLevel = 1
        maxSum = float("-inf")
        level = 1

        while queue:
            sum1 = 0
            nextLevel = []  # track of left and
            for node in queue:
                sum1 += node.val
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if sum1 > maxSum:
                maxSum = sum1
                maxLevel = level

            queue = nextLevel
            level += 1
        return maxLevel
