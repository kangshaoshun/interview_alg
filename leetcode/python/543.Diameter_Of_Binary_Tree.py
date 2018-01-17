#coding:utf-8
"""
    求出二叉树的最长直径
    思路：
        递归，我发现二叉树的很多问题都是使用递归的思路去解决
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        """
        self.ans = 0
        def depth(p):
            if not p:
                return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
        depth(root)
        return self.ans

