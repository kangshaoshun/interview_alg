#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
生成二叉树的镜像
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ReverseBinaryTree(object):
    def reverse(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.reverse(root.left)
        self.reverse(root.right)
        return root

def preOrder(root):
    if root:
        print root.val
        preOrder(root.left)
        preOrder(root.right)

if __name__ == '__main__':
    r = ReverseBinaryTree()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root = r.reverse(root)
    preOrder(root)
