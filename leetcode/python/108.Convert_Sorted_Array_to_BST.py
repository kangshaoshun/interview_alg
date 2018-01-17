#coding:utf-8
"""
    将有序数组转换成平衡的排序二叉树(AVL)
    思路：因为数组已经有序，所以此题有巧解，而并不用重构AVL
    Time Complexity:O(N)
    Space Complexity:O(1)
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def sortedArray2BST(self, nums):
        if not nums:
            return None
        middle = len(nums) / 2
        node = TreeNode(nums[middle])
        node.left = sortedArray2BST(nums[:middle])
        node.right = sortedArray2BST(nums[middle+1:])
        return node
