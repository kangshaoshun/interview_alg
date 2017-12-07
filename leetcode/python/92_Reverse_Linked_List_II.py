#coding:utf-8
"""
    题意：反转单链表进阶题，反转m 到 n 之间的节点，其他的不变
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        dummy_node = ListNode(0)
        dummy_node.next = head
        pre = dummy_node
        for i in range(m-1):
            pre = pre.next

        #反转m 到 n之间的节点
        reverse = None
        cur = pre.next
        for i in range(n-m+1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse
        return dummy_node.next



