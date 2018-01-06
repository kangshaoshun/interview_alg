#coding:utf-8
"""
    题意：合并两个二叉树
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
            :type t1:TreeNode
            :type t2:TreeNode
            :rtype :TreeNode
        """
        """
            Time Complexity:O(m+n)
            Space Complexity:O(max(m,n))
        """
        if not t1 and not t2:
            return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)  # and 取第一个假值，没有假值就取最后一个
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans
