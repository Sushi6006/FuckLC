# 2021-03-06

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBalanced(self, root) -> bool:
        
        def height(node):
            if not node:
                return 0

            return max(height(node.left), height(node.right)) + 1

        
        if not root:
            return True

        return self.isBalanced(root.left) and self.isBalanced(root.right) and \
               abs(height(root.left) - height(root.right)) <= 1
