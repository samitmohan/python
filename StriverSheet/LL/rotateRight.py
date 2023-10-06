# https://www.youtube.com/watch?v=UcGtPs2LE_c
# O(n)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head  # no rotations
        # Get length
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length  # reduce it to a number less than the length
        if k == 0:
            # no rotations
            return head
        # Move to pivot and perform rotate
        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        tail.next = head
        return new_head
