#coding:utf-8
"""
    题意：旋转单链表k位
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
            思路：1.找到从后往前数第k个节点，这个几点即将成为头结点
                  2.指针转换
            Time Complexity:O(N)
            Space Complexity:O(1)
        """
        if not head or not head.next:
            return head
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        odd = k % length
        if not odd:
            return head
        left = right = head
        while odd:
            right = right.next
            odd -= 1
        while right.next:
            left, right = left.next, right.next
        ret = left.next
        left.next = None
        right.next = head
        return ret

            

