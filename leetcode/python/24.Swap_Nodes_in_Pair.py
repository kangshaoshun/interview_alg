#coding:utf-8
class ListNdode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
            题意：swap every two adjacent nodes and return its head.

            eg.Given 1->2->3->4, you should return the list as 2->1->4->3

            Time Complexity:O(N)
            Space Complexity:O(1)
            解题思路：
                交换两个节点毕然要有这两个节点之前的节点        
        """
        #常规易理解
        if not head or not head.next:
            return head
        res_node = ListNode(0)
        p_node = res_node
        res_node.next = head
        while p_node.next and p_node.next.next:
            tmp = p_node.next.next
            p_node.next.next = tmp.next
            tmp.next = p_node.next
            p_node.next = tmp
            p_node = p_node.next.next
        return res_node.next

        #原理是一样的，写法高级点的
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next



        
