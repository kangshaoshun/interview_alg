#coding:utf-8
"""
    题意：给定一个单链表，将单链表切割成k份
        eg. root = [1, 2, 3] k = 5
        output:[[1], [2], [3], [], []]
    解题思路：
        1.得出单链表长度
        2.计算出每一part的链表长度
        3.得打每一part的链表
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
            :type root:ListNode
            :type k:int
            :rtype: List[LietNode]
        """
        length = 0
        tmp = root
        while tmp:
            length += 1
            tmp = tmp.next
        shang = length / k
        yushu = length % k
        nums = [shang for i in range(k)]
        for i in range(yushu):
            nums[i] += 1
        pre = None
        cur = root
        for index, item in enumerate(nums):
            if pre:
                pre.next = None
            num[index] = cur
            for i in range(item):
                pre = cur
                cur = cur.next
        return nums

