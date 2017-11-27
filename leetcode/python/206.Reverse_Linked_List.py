#coding:utf-8
class Solution(object):
    def reverseList(self, head):
        """
            :type head:ListNode
            :rtype: ListNode
        """
        """
            反转单链表，这也是面试中常考的一道题
            常规做法：
                1.迭代
                2.递归
        """
        prev = None
        while head:
            curr = head
            head = head.next
            crr.next = prev
            prev = curr
        return prev
