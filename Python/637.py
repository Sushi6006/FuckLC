# 2021-03-09

from statistics import mean

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        # find root max depth
        def depth(node):
            if not node:
                return 0

            return max(depth(node.left), depth(node.right)) + 1
        
        # add to list to calculate average
        def avglvl(node, target_lv, prev_lv):

            if not node:
                return

            curr_lv = prev_lv + 1

            if curr_lv == target_lv:
                self.curr_nodes.append(node.val)
                return

            avglvl(node.left, target_lv, curr_lv)
            avglvl(node.right, target_lv, curr_lv)

        
        self.curr_nodes = []
        self.result = []
        max_depth = depth(root)
        for i in range(max_depth):
            self.curr_nodes = []
            avglvl(root, i, -1)
            self.result.append(mean(self.curr_nodes))
        
        return self.result