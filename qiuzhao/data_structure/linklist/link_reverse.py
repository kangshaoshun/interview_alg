#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
链表翻转  递归和非递归

非递归：设置三个指针 pre, cur, next 逐一翻转即可
递归：很简单，自己看
"""

class Solution(object):
    def reverse_linklist_non(self, head):
        if not head or not head.next:
            return head
        pre, cur = head, head.next
        pre.next = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def reverse_linklist_rec(self, head):
        if not head or not head.next:
            return head
        def reverse(head, pre):
            if not head:
                return pre
            tmp = head.next
            head.next = pre
            return reverse(tmp, head)
        return reverse(head, None)

