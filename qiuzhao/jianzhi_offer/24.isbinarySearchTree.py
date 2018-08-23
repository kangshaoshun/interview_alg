#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
判断一个数组是不是二叉搜索树的后序遍历序列

思路：递归
    二叉搜索树的后序遍历序列存在规律，根节点可以将数组分为两半，一半比根节点大，一半比根节点小。
    将左右子树递归下去
    如果数组长度小于等于2，则必然是。
"""

def isPostOrder(nums):
    if not nums:return False
    return verify(nums)

def verify(nums):
    length = len(nums)
    if length <= 2:return True
    root = nums[-1]
    for i in range(0, length - 1):
        if nums[i] > root:
            for j in range(i, length - 1):
                if nums[j] < root:
                    return False
            break
    return verify(nums[0:i]) and verify(nums[i:-1])

if __name__ == '__main__':
    print isPostOrder([5, 4, 3, 2, 1])

