#coding:utf-8 
"""
    广度优先遍历 for binary tree
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




def bfs(root):
    p = [root]
    while p:
        p1 = []
        while p:
            node = p.pop(0)
            print node.val
            if node.left:
                p1.append(node.left)
            if node.right:
                p1.append(node.right)
        p = list(p1)

if __name__ == '__main__':
    root = TreeNode(1)
    root1 = TreeNode(1)
    print root == root1
    """
    root.left = TreeNode(2)
    root.left.left = TreeNode(7)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(5)
    """
    #bfs(root)


