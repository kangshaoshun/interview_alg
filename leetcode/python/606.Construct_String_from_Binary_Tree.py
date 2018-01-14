#coding:utf-8
"""
    题意：通过二叉树构建字符串
    [1, 2, 3, 4]  ===> 1(2(4))(3)
    [1, 2, 3, None, 4] ==>  1(2()4)(3)
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def tree2str(self, t):
        """
            Time Complexity:O(N)        
            Space Complexity:O(N)
        """
        if not t:
            return ""
        left = "({})".format(self.tree2str(t.left)) if (t.left or t.right) else ""
        right = "({})".format(self.tree2str(t.right)) if t.right else ""
        return "{}{}{}".format(t.val, left, right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    s = Solution()
    print s.tree2str(root)
