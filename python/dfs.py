#coding:utf-8
"""
    深度优先遍历 for binary tree
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(root):
    stack = [root]
    while stack:
        node = stack.pop()
        print node.val
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)               
    root.left.left = TreeNode(7)      
    root.right = TreeNode(4)          
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(5)
    dfs(root)
