# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(0, head)  # to return
        left = prev
        right = head
        # right reacheds n (3)
        while n > 0:
            right = right.next
            n -= 1

        # left reaches 3 and right reaches null (why 3 and not 4 : because left = prev (dummy ptr))
        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return prev.next  # 1->2->3->5
