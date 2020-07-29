# 2020-07-26

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def find_sum(self, root, curr_path, curr_sum, res_path):
        
        if root is None:
            return
        
        # if path ends and sum is correct
        if not root.left and not root.right and curr_sum == root.val:
            curr_path.append(root.val)
            res_path.append(curr_path[:])
            return
        
        # add current node
        curr_sum -= root.val
        curr_path.append(root.val)
        
        # go down
        self.find_sum(root.left, curr_path[:], curr_sum, res_path)
        self.find_sum(root.right, curr_path[:], curr_sum, res_path)
        
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res_path = []
        self.find_sum(root, [], sum, res_path)
        
        return res_path