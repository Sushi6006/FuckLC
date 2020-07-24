# 06/22/2020 02:28

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        if t1 or t2:
            res = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
            res.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
            res.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
            
            return res
        else:
            return t1 or t2
        
        