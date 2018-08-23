#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
二叉树的层序遍历
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelTraversal(root):
    if not root:return
    queue = [root]
    while queue:
        tmp = []
        for node in queue:
            print node.val
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        queue = tmp
