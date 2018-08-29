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
    def tree2linklist(self, root):
        if not root:return
        stack = []
        res = ''
        flag = False
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                if not flag:
                    res = root
                    node = res
                    flag = True
                else:
                    node.right = root
                    root.left = node
                    node = node.right
                root = root.right
        return res


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(6)
    root.right = TreeNode(14)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(8)
    root.right = TreeNode(14)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(16)
    s = Solution()
    res = s.tree2linklist(root)
    tmp = ''
    while res:
        print res.val
        tmp = res
        res = res.right

    while tmp:
        print tmp.val
        tmp = tmp.left
