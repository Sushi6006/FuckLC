"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return []
        res.append(root.val)  # preorder
        if root.children:
            for child in root.children:
                # append each val to the list
                for val in self.preorder(child):
                    res.append(val)
        
        return res
            