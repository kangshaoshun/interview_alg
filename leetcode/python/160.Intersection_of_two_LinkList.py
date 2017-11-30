#coding:utf-8
"""
    题意：有两个单链表，找出这两个单链表的汇聚节点
    思路：
        1.遍历2次分别得到这两个单链表的长度
        2.将长度更长的那个链表先向后移动 长度差 个节点
        3.同时移动两个链表，相等最初相等的节点就是汇聚节点
    复杂度：
        Time Complexity:O(N)
        Space Complexity:O(1)
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA,headB):
        curA = headA
        curB = headB
        length_A = curA
        length_B = curB
        while curA:
            length_A += 1
            curA = curA.next
        while curB:
            length_B += 1
            curB = curB.next
        if lengthA > length_B:
            diff = length_A - length_B
            while diff:
                headA = headA.next
                diff -= 1
        else:
            diff = lengthB - length_A
            while diff:
                headB = headB.next
                diff -= 1
        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
