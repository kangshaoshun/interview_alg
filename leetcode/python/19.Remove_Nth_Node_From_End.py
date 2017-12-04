#coding:utf-8
"""
    题意：移除从后往前数的第n个节点
    eg. 1 -> 2 -> 3 -> 4 -> 5 and n = 2
    return: 1 -> 2 -> 3 -> 5
"""
"""
    思路：1.得到链表长度
          2.插入一个头前节点pre
          3.头前节点移动 l - n
          4.删除该节点即可
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        pre = ListNode(0)
        pre.next = head
        pre_bk = pre
        l = 0
        while head:
            head = head.next
            l += 1
        diff = l - n
        while diff:
            pre = pre.next
            diff -= 1
        pre.next = pre.next.next
        return pre_bk
