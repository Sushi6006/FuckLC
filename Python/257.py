# 2021-03-10

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        self.res = []
        
        def dfs(node, curr):
            if not node:
                return
            
            if not node.left and not node.right:
                self.res.append(curr + str(node.val) + "->")
            
            dfs(node.left, curr + str(node.val) + "->")
            dfs(node.right, curr + str(node.val) + "->")
            
        dfs(root, "")
        return [s[:-2] for s in self.res]