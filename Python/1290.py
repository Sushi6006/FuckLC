# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = []
        res = 0
        while head:
            num.append(head.val)
            head = head.next
        for i in range(len(num)):
            res += num.pop() * (2 ** i)
        
        return res