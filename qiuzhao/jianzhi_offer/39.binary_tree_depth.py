#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
求二叉树的深度
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getDepth(self, root):
        if not root:
            return 0
        n_left = self.getDepth(root.left)
        n_right = self.getDepth(root.right)
        return n_left + 1 if n_left > n_right else n_right + 1

    def isBalanceTree(self, root):
        

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(4)
    print s.getDepth(root)
