#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
Given a binary tree, find its minimum depth
"""
class Solution(object):
    def minDepth(self, root):
        """
        :type root:TreeNode
        :rtype :int
        """
        if not root:
            return 0
        min_depth = float('inf')
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right and depth < min_depth:
                min_depth = depth
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return min_depth
