# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # same as level order but for odd levels : swap the order : [9, 20] = [20, 9] : level sub-list
        # O(N) Time and Space
        ans = []
        q = deque([root] if root else [])
        while q:
            level = []
            size = len(q)
            for i in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # for every odd level : reverse the order (if len(ans) % 2 = 1)
            level = reversed(level) if len(ans) % 2 else level
            ans.append(level)

        return ans
