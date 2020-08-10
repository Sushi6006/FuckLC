# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = self.traverse(root)
        prev_node = TreeNode(res[len(res) - 1])
        for i in range(len(res) - 2, -1, -1):
            node = TreeNode(res[i])
            node.right = prev_node
            prev_node = node
        
        return prev_node
                
            
    
    def traverse(self, root) -> List:
        res = []
        if not root:
            return res
        if root.left:
            for val in self.traverse(root.left):
                res.append(val)
        res.append(root.val)
        if root.right:
            for val in self.traverse(root.right):
                res.append(val)
        return res