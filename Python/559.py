# 2021-03-07

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        depths = [0]
        for i in range(len(root.children)):
            depths.append(self.maxDepth(root.children[i]))
        
        return max(depths) + 1