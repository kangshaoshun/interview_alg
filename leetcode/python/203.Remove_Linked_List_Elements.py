#coding:utf-8
"""
    题意：删除单链表中指定的元素
        经常考的链表题目,解题思路：
            创建一个头前节点
            遍历链表，如果cur.next.val == val 则删除cur.next节点
            否则保留cur.next节点，使cur = cur.next
            Time Complexity:O(N)
            Space Complexity:O(1)
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        cur = ListNode(0)
        cur.next = head
        res = cur
        while cur and cur.next:
            if cur.next.val == val:
                cur.next.next = cur.next
            else:
                cur = cur.next
        return res.next

    
