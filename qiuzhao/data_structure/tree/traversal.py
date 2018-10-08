#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
二叉树遍历
"""
class Solution(object):
    def preOrder(self, root):
        """
        :type root:TreeNode
        """
        if not root:return []
        stack, res = [], []
        while stack or root:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            if stack:
                root = stack.pop()
                root = root.right
        return res

    def preOrderRecur(self, root):
        if not root:return
        if root:
            print root.val
        self.preOrderRecur(root.left)
        self.preOrderRecur(root.right)

    def inOrder(self, root):
        if not root:return []
        stack, res = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

    def inOrderRecur(self, root):
        if not root:return
        if root.left:
            self.inOrderRecur(root.left)
        print root.val
        if root.right:
            self.inOrderRecur(root.right)

    def postOrder(self, root):
        if not root:return
        stack, res, pre = [], [], None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack[-1]
            if not root.right or root.right == pre:
                root = stack.pop()
                res.append(root.val)
                pre = root
                root = None
            else:
                root = root.right
        return res

    def postOrderRecur(self, root):
        if not root:
            return
        if root.left:
            self.postOrderRecur(root.left)
        if root.right:
            self.postOrderRecur(root.right)
        print root.val

    def levelTraver(self, root):
        """
        层序遍历/广度优先遍历
        """
        if not root:return 
        queue = [root]
        res = []
        while queue:
            tmp = []
            for node in queue:
                res.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
        return res

    def depthTraver(self, root):
        if not root:return
        stack = [root]
        while stack:
            root = stack.pop()
            print root.val
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.right = TreeNode(4)
    s.depthTraver(root)
