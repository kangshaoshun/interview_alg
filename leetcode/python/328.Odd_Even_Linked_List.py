#coding:utf-8
class ListNode(object):
    def __init(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
            type head: ListNode
            rtype: ListNode
        """
        """
            题意：奇偶链表（将奇数位的node搬到偶数位的node前面）
            Time Complexity:O(N)
            Space Complexity:O(1)
        """
        if not head or not head.next or not head.next.next:
            return head
        odd = head
        res = odd
        even = head.next
        even_head = even
        head = head.next.next
        flag = True
        while head:
            if flag:
                odd.next = head
                odd = odd.next
                flag = False
            else:
                even.next = head
                even = even.next
                flag = True
            head = head.next
        odd.next = even_head
        even.next = None
        return res
