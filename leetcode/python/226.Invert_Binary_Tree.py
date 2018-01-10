#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
    反转二叉树（所有节点，左右倒置）
    Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
            递归
            Time Complexity:O(N)
            Space Complexity:O(1)
        """
        if not root:
            return root
        if root.left and root.right:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        elif root.left:
            root.left, root.right = None, root.left
            self.invertTree(root.right)
        else:
            root.left, root.right = root.right, None
            self.invertTree(root.left)
        return root
