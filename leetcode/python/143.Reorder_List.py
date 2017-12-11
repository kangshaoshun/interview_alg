#coding:utf-8
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
            题意：重新排序链表，0 -> n -> 1 -> n-1 -> 2 -> n-2...
            思路：分三步走：
                    第一：找到右半边链表头节点的前节点(快慢指针，并且终止条件为fast.next and fast.next.next)
                    第二:反转右半边链表(三指针链表反转)
                    第三：合并链表
            Time Complexity:O(N)
            Space Complexity:O(1)
        """
        if not head or not head.next:
            return
        #找出右半边链表的头前节点
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        right = slow.next
        slow.next = None
        #反转单链表
        pre = None
        cur = right
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        #合并链表
        while head and pre:
            left_tmp = head.next
            head.next = pre
            right_tmp = pre.next
            pre.next = left_tmp
            head = left_tmp
            right = right_tmp
        if head:
            head.next = None
        if pre:
            pre.next = None
