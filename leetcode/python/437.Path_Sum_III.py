#coding:utf-8
"""
    题意：找出路径上元素之和为val 的路径数之和
    思路：这是一道DFS应用的题目
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def get_sum(self, root, pre, sum):
        if not root:
            return 0
        current = pre + root.val
        return int(current == sum) + self.get_sum(root.left, current, sum) + self.get_sum(root.right, current, sum)

    def pathSum(self, root, sum):
        """
            :type root  TreeNode
            :type sum   int
        """
        if not root:
            return 0
        return self.get_sum(root, 0, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

