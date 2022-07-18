from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        counter = 1
        middle = head
        while head:
            if counter % 2 == 0:
                middle = middle.next
            counter += 1
            head = head.next

        return middle
        
