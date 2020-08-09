# 2020-08-09

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        
        curr = root.val if L <= root.val <= R else 0
        return curr + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)