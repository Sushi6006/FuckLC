"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return []
        if root.children:
            for child in root.children:
                # append each val to the list
                for val in self.postorder(child):
                    res.append(val)
        res.append(root.val)  # postorder
        
        return res
            