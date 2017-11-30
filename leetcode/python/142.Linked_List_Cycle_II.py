#coding:utf-8
class ListNode(self, x):
    def __init__(self):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self):
        """
            这题是上一道题的进阶版，除了判断链表中是否有环之外还要找出环的入口
            如果没有follow up:不允许使用额外空间，这道题其实也非常简单，就不会是一道media了
            加上follow up 就需要一点思考了；
                假设链表起始位置X,环开始点Y,快慢指针相遇点Z,X到Y距离a,Y-Z距离b,Z-Y距离c
                由于快指针速度是慢指针的2倍，所以有：
                    2(a+b) = a + b + n(b+c)        ==>   a = (n-1)(b+c) +c
                    b+c 是环的长度，也就是说，如果在相遇点将慢指针移回头结点，慢指针走a步到达Y的时候，快指针也会从Z走完n-1圈多c步到达Y，这就找到了环的入口

        """
        #no follow up
        if not head or not head.next:
            return None
        s = set()
        while head:
            if head not in s:
                s.add(head)
                head = head.next
            else:
                return head


        #has follow up
        if not head or not head.next:
            return None
        slow = head.next
        fast = head.next.next
        while fast and fast.next:
            if slow == fast:
                slow = head
                break
            else:
                slow = slow.next
                fast = fast.next.next
        if slow != head:
            return None
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
