#coding:utf-8
"""
    Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

    思路：广度优先遍历二叉树，但是输出顺序相反
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        """
            广度优先遍历的应用
        """
        q = [root]
        res_stack = []
        while q:
            q1 = []
            tmp_list = []
            while q:
                node = q.pop(0)
                tmp_list.append(node.val)
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
            res_stack.append(tmp_list)
            q = q1
        res = []
        while res_stack:
            res.append(res_stack.pop())
        return res



