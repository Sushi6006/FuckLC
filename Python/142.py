from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # loop is found
                # at this stage, `slow` travelled (x + y) steps,
                # and `fast` travelled 2 * (x + y) steps
                # where x is steps to start of the circle, and y is the rest
                # `fast` travelled (x + y) more steps in a loop
                # that means (x + y) is the length of the loop
                break
        else:
            return  # fast ends on None, end of list is not looping

        # `slow` is now y steps into the loop
        # after x steps, `slow` will be at the beginning of the loop again
        # where x is the distance between head and start of the loop
        # hence, when head is slow, they both moved x steps
        # by then, beginning of the loop is found
        while head != slow:
            head = head.next
            slow = slow.next

        return slow
