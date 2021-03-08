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
    tmp_queue = [root]

    while tmp_queue:
        i += 1
        node = tmp_queue.pop()
        if not node.val:
            continue

        if 2*i -1 >= len(li):
            return root
        
        node.left = TreeNode(li[2*i-1])
        tmp_queue.append(node.left)

        if 2*i >= len(li):
            return root
        
        node.right = TreeNode(li[2*i])
        tmp_queue.append(node.right)
        
    return root

def bin_to_dec(li):
    return sum([2 ** i * n for i, n in enumerate(li[::-1])])

# def dfs2(node, cur):
    
#     if not node:
#         return

#     if node.left is None and node.right is None:
#         print("NO CHILD LEFT:", cur, node.val)
#         res.append(cur + [node.val])
#         return 
    
#     if node.left:
#         dfs2(node.left, cur + [node.val])
    
#     if node.right:
#         dfs2(node.right, cur + [node.val])

# def dfs(node, cur):
    
#     if not node:
#         return

#     cur += [node.val]

#     if (node.left is None) and (node.right is None):
#         print("NO CHILD LEFT:", cur, node.val)
#         res.append(cur)
#         cur.pop()
#         return 
    
#     if node.left:
#         dfs(node.left, cur)
    
#     if node.right:
#         dfs(node.right, cur)
    
#     cur.pop()


def dfs(node, cur):

    if node is None:
        return
    
    if (node.left is None) and (node.right is None):
        print("NO CHILD LEFT:", node.val, cur)
        res.append(cur)
        return
    
    if node.left:
        dfs(node.left, cur + [node.val])
    
    if node.right:
        dfs(node.right, cur + [node.val])


res = []
li = [5,3,6,2,4,None,8,1,None,None,None,7,9]
li2 = [10,5,15,3,7,None,18]
dfs(list_to_tree(li), [])

print(res)