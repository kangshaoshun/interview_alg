#coding:utf-8
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
            删除链表中的重复元素，这也是面试题中经常考的一道题，也很简单
            思路：
                利用一个set判断是否元素重复出现了（因为是有序的），然后添加即可
            Time Complexity:O(N)
            Space Complexity:O(N)
        """
        if not head or not head.next:
            return head
        res = ListNode(0)
        ret = res
        s = set()
        while head:
            if head.val not in s:
                s.add(head.val)
                res.next = head
                res = res.next
            head = head.next
        res.next = None
        return ret.next




#改进版
class Solution(object):
    def deleteDuplicates(self, head):
        """"
            借助和82题一样的思想
        """"
        helper = ListNode(0)
        helper.next = head
        pre = head
        while head and head.next:
            if head.val != head.next.val:
                head = head.next
                pre = head
            else:
                tmp = head.val 
                while head and head.val == tmp:
                    head = head.next
                pre.next = head
                pre = head
        return helper.next
