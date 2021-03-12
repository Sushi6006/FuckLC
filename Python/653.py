# 2021-03-12

# I know this code is pure garbage
# That is because I have made a few stupid mistakes
# But it works

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        self.root = root
        self.found = False
        
        def bisearch(node, target):
            
            if not node:
                return False
            
            if node.val < target:
                return bisearch(node.right, target)
            elif node.val > target:
                return bisearch(node.left, target)
            else:
                return True
            
            return False
        
        
        def find(root, k):
            if not root:
                return False
            
            if root.val * 2 != k:
                self.found = bisearch(self.root, k - root.val)
                if self.found:
                    return True

            return find(root.left, k) or find(root.right, k)
        
        return find(root, k)
        
        