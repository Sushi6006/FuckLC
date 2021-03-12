# 2021-03-10

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.li1 = []
        self.li2 = []
        
        def dfs(node, res):
            if not node:
                return
            
            if not node.left and not node.right:
                res.append(node.val)
                return
            
            dfs(node.left, res)
            dfs(node.right, res)
        
        dfs(root1, self.li1)
        dfs(root2, self.li2)
        
        return self.li1 == self.li2
        
        