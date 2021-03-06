class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(li):
    if not li:
        return TreeNode(None)

    i = 0
    root = TreeNode(li[i])
    queue = [root]

    while queue:
        i += 1
        node = queue.pop()
        if not node.val:
            continue

        if 2 * i -1 >= len(li):
            return root
        
        node.left = TreeNode(li[2*i-1])
        queue.append(node.left)

        if 2 * i >= len(li):
            return root
        
        node.right = TreeNode(li[2 * i])
        queue.append(node.right)

    return root