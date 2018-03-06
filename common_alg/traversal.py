#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
这里列举了遍历二叉树的常考算法

前序， 中序， 后序 dfs bfs
"""
class TreeNode(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

class Solution(object):
    def __init__(self):
        self.res = []

    #递归形式
    def preorderTraversal(self, root):
        """
            前序遍历
        :type root:TreeNode
        :rtype:List[int]
        """
        if root:
            self.res.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.res

    def inorderTraversal(self, root):
        """
            中序遍历
        :type root:TreeNode
        :rtype:List[int]
        """
        if root:
            self.inorderTraversal(root.left)
            self.res.append(root.val)
            self.inorderTraversal(root.right)
        return self.res

    def postorderTraversal(self, root):
        """
            后序遍历
        :type root:TreeNode
        :rtype:List[int]
        """
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.res.append(root.val)
        return self.res

    #非递归形式
    def preorderNonRecursion(self, root):
        """
            非递归先序遍历
        :type root:TreeNode
        :rtype:List[int]
        """
        stack = []
        node = root
        res = []
        while node or stack:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                node = node.right
        return res

    def inorderNonRecursion(self, root):
        """
            非递归中序遍历
        :type root:TreeNode
        :rtype:List[int]
        """
        stack = []
        node = root
        res = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res

    def postorderNonRecursion(self, root):
        """
            非递归后序遍历
        :type root:TreeNode
        :rtype:List[int]
        """
        stack = []
        node = root
        res = []
        pre = None
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            #关键在这里，要遍历node需确保无右子节点或右子节点已经被遍历了
            if not node.right or node.right == pre:
                res.append(node.val)
                pre = node
                stack.pop()
                node = None
            else:
                node = node.right
        return res

    #广度优先遍历和深度优先遍历有着很广的应用，遍历二叉树只是一方面
    def bfs(self, root):
        """
        广度优先遍历二叉树(lc 515)
        :type root:TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            tmp_queue = []
            while queue:
                node = queue.pop(0)
                res.append(node.val)
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            queue = tmp_queue
        return res
    
    def dfs(self, root):
        """
        深度优先遍历遍历二叉树(lc 112, lc 257)
        :type root:TreeNode
        :rtype:List[int]
        """
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right = TreeNode(2)
    root.right.left = TreeNode(9)
    print s.dfs(root)
