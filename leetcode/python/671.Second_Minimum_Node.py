#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
    Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

    Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

    If no such second minimum value exists, output -1 instead.

    关键是理解题意，对于这种二叉树，显然，root节点就是最小值节点，要寻找第二小节点，遍历节点即可。tips:只遍历子节点中最小的节点
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        if not root or not root.left or (root.left.val == root.val and root.right.val == root.val):
            return -1
        self.value = root.val
        if root.left.val == self.value:
            res = root.right.val
        else:
            res = root.left.val
        def search(root):
            if not root:
                return None
            if root.val != self.value and root.val < self.value:
                self.res = root.val
            search(root.left)
            search(root.right)
        search(root)
        return self.res
        
