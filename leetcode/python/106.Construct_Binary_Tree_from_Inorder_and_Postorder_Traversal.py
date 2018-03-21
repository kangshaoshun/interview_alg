#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
根据后序遍历和中序遍历构建二叉树
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(inorder, postorder):
        if not inorder:
            return None
        val = postorder.pop()
        root = TreeNode(val)
        root.right = buildTree(inorder[inorder.index(val)+1:], postorder)
        root.left = buildTree(inorder[:inorder.index(val)], postorder)
        return root
