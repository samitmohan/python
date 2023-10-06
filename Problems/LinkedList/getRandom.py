import random


# https://leetcode.com/problems/linked-list-random-node/
class Solution:
    def __init__(self, head):
        # biggest problem : don't know the range of the list (how to pick random)
        # convert into array
        self.arr = []  # range
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        # random function to choose node random;ly from list
        pick = int(random.random() * len(self.arr))  # random index
        return self.arr[pick]
