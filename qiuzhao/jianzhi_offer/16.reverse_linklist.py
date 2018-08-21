#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
反转单链表

三个指针移动，以 while pre为循环终止条件，记得将head.next 置空
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse_linklist(self, head):
        if not head or not head.next:
            return head
        left, mid = head, head.next
        head.next = None
        pre = mid.next
        while pre:
            mid.next = left
            left = mid
            mid = pre
            pre = mid.next
        mid.next = left
        return mid


