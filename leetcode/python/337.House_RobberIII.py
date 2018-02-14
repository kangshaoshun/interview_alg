#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root:TreeNode
        :rtype: int
        dfs
        Time Complexity:O(N)
        Space Complexity:O(N)
        """
        return max(self.dfs(root))

    def dfs(self, x):
        if not x:
            return 0, 0
        left = self.dfs(x.left)
        right = self.dfs(x.right)
        res = [left[1] + right[1] + val]
        res.append(max(left) + max(right))
        return res
