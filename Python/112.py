# 2020-07-29

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.find_sum(root, sum)
    
    def find_sum(self, root, curr_sum):
        if root is None:
            return False
        
        if not root.left and not root.right and curr_sum == root.val:
            return True
        
        curr_sum -= root.val
        
        return self.find_sum(root.left, curr_sum) or self.find_sum(root.right, curr_sum)