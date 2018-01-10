#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
    Given a binary tree, find its maximum depth.
    思路：
        后序遍历的一种应用
"""

class Solution():
    def maxDepth(self, root):
        """
            Time Complexity:O(n)
            Space Complexity:O(n)
        """
        stack = []
        node = root
        pre = None
        max_len = 0
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if not node.right or node.right == pre:
                stack.pop()
                pre = node
                node = None
            else:
                node = node.right
        return max_len
