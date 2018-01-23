#coding:utf-8
"""
    题意：判断一棵树是否是镜像树
    思路：递归循环判断
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
            :type root:TreeNode
            :rtype :boolean
        """
        def mirror(left, right):
            if not left and not right:
                return True
            elif (not left and right) or (left and not right) or (left.val != right.val):
                return False
            else:
                return mirror(left.left, right.right) and mirror(left.right, right.left)

        if not root or (not root.left and not root.right):
            return True
        return mirror(root.left, root.right)
