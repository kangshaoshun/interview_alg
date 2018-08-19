#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
根据中序遍历和前序遍历重构二叉树

根据中序遍历和后序遍历重构二叉树


思路：递归，其实只要是二叉树的题目，基本都可以用递归
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def re_construct_tree(self, pre_order, in_order):
        """
        根据前序和中序重构二叉树
        """
        if not pre_order:return
        root = TreeNode(pre_order[0])
        index = in_order.index(pre_order[0])
        root.left = self.re_construct_tree(pre_order[1: index + 1], in_order[:index])
        root.right = self.re_construct_tree(pre_order[index + 1:], in_order[index + 1:])
        return root


    def re_construct_tree2(self, in_order, post_order):
        #原理同上
        pass

