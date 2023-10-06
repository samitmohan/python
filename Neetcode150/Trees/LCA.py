# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
'''
LCA : where split is ocurring
in the first example : split occurs at 6 since 2 < 6 and 8 > 6
in the next example : both 2 and 4 are in left ST : new common ancestor : 2 not 6
  2 <=2 and 4 > 2 :: hence 2 is where the split takes place : lCA
  and if any of p, q val = node.val : obviously that is the ancestor
  (example : 6 is the ancestor for p = 6 and q = 7)

Time : Height : O(log(n))
'''


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while True:  # going to repeat until we find answer
            if p.val > curr.val and q.val > curr.val:  # go right
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:  # split occurs : answer found (curr)
                return curr
        # no need to return anything since while True will run forever until answer found
