#coding:utf-8
class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
            合并两个有序链表，这是面试中常考的题目，也很简单
            题目思路：迭代，递归
        """
        res = ListNode(0)
        ret = res
        while l1 and l2:
            if l1.val <= l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next
        if l1:
            res.next = l1
        if l2:
            res.next = l2
        return ret.next
