#coding:utf-8
"""
    广度优先遍历的一个应用，求层级平均值
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        """
        p = [root]
        res = []
        while p:
            p1 = []
            total = 0
            cnt = 0
            while p:
                node = p.pop(0)
                total += node.val
                cnt += 1
                if node.left:
                    p1.append(node.left)
                if node.right:
                    p1.append(node.right)
            res.append(total * 1.0 / cnt)
            p = list(p1)
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(5)
    s = Solution()
    print s.averageOfLevels(root)

