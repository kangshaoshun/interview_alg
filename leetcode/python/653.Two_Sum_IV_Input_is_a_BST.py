#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
    查找排序二叉树中是否有两个节点的值之和等于k
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
            Time Complexity:O(N)
            Space Complexity:O(N)
        """
        if not root:
            return False
        bfs, s = [root], set()
        for node in bfs:
            if k - node.val in s:
                return True
            s.add(node.val)
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
        return False


