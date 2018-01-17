#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
    求二叉树的左叶子节点的和

    可以衍生出：求二叉树的右叶子节点之和

    解题思路：
        递归，3种基本情况
            1.root 空
            2.root 不空，左子节点为叶子节点，则这个左子节点就是所需，递归下去
            3.递归处理 root.left 和 root.right
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
            求左 叶子节点 之和
        """
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    def sumOfRightLeaves(self, root):
        """
            求 右 叶子节点 之和
        """
        if not root:
            return 0
        if root.right and not root.right.left and not root.right.right:
            return root.right.val + self.sumOfRightLeaves(root.left)
        return self.sumOfRightLeaves(root.left) + self.sumOfRightLeaves(root.right)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.left.right = TreeNode(20)
    root.right.right = TreeNode(7)
    s = Solution()
    print s.sumOfLeftLeaves(root)
    print s.sumOfRightLeaves(root)
