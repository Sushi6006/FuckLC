# 2021-03-08

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        def bin_to_dec(li):
            return sum([2 ** i * int(n) for i, n in enumerate(li[::-1])])

        def dfs(node, curr):

            if not node:
                return

            if not node.left and not node.right:
                self.res += int(curr + str(node.val), 2)
                # self.res += bin_to_dec(curr + str(node.val))
                # res.append(curr + str(node.val))  # this was when res was ["", ""]

            dfs(node.left, curr + str(node.val))
            dfs(node.right, curr + str(node.val))
                
                
        self.res = 0
        dfs(root, "")
        # return sum(list(map(bin_to_dec, res)))
        return self.res