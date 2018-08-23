#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
复杂链表的复制

思路：
在每个节点后面添加一个节点，然后可以定位random.
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

class Solution(object):
    def copy_linklist(self, head):
        if not head:return head
        pre = head
        while pre:
            tmp = ListNode(pre.val)
            tmp.next = pre.next
            pre.next = tmp
            pre = pre.next.next
        pre = head
        while pre:
            if pre.random:
                pre.next.random = pre.random.next
            pre = pre.next.next
        pre = head
        tmp = res = head.next
        while tmp.next:
            pre.next = tmp.next
            tmp.next = pre.next.next
            pre = pre.next
            tmp = tmp.next
        pre.next = None
        return res
