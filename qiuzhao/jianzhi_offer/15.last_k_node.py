#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
删除链表的倒数第k个结点
"""
class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def remove_k_node(self, head, k):
        if not head or not head.next:
            return None
        fast = slow = pre = LinkNode(-1)
        pre.next = head
        while k:
            fast = fast.next
            k -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        if slow.next == head:
            head = head.next
        else:
            slow.next = slow.next.next
        return head

