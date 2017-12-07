#coding:utf-8
"""
    题意：分隔单链表，将单链表中大于x的节点移动到后段，小于x的节点移动到前段，保持相对顺序不变
"""
"""
    思路：借助辅助节点，先将小于x的节点和大于x的节点都串起来，然后将小节点和大节点串 连接起来
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self):
        """
            type head:ListNode
            type x:int
            rtype:ListNode
        """
        """
            这种做法思路清晰并且时间复杂度和空间复杂度都是极简的
            Time Complexity:O(N)
            Space Complexity:O(1)
        """
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        return h1.next
