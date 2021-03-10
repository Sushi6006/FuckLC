# 2021-03-10

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        self.unique = root.val
        self.res = True
        
        def dfs(node):
            if not node:
                return
            
            if node.val != self.unique:
                self.res = False
                return 
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.res