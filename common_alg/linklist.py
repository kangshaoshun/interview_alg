#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
链表相关面试算法
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList(object):
    def deleteListNode(self, head, node):
        """
        给定链表头结点与要删除节点，在O(1)时间删除该节点
        :type head:ListNode
        :type node:ListNode
        :rtype:ListNode
        思路：狸猫换太子，将后一个节点的值跟要删除节点换，然后删除后一个节点（尾节点除外）
        """
        if not node.next:
            return 'except tail node'
        node.val = node.next.val
        node.next = node.next.next
        return head

    def reverseLinkList(self, head):
        """
        反转单链表
        :type head:ListNode
        :rtype : ListNode
        思路：反转单链表一般有迭代和递归两种思路
        """
        #迭代
        pre = ListNode(0)
        while head:
            node = head
            head = head.next
            node.next = pre.next
            pre.next = node
        return pre.next

        #递归
        def help(head, newhead):
            if not head or not head.next:
                newhead = head
            else:
                newhead = help(head.next, newhead)
                head.next.next = head
                head.next = None
            return newhead
        return help(head, None)

    def removeNthFromEnd(self, head, n):
        """
        删除单链表的倒数第n个节点
        :type head:ListNode
        :type n:int
        :rtype: ListNode
        思路：快慢指针,快指针先走n步
        """
        pre = quick = slow = ListNode(0)
        while n:
            quick = quick.next
            n -= 1
        while quick.next:
            quick = quick.next
            slow = slow.next
        slow.next = slow.next.next
        return pre.next

    def isPalindrome(self, head):
        """
        判断单链表是否是回文单链表(要求T=O(N), S=O(1))
        :type head: ListNode
        :rtype: bool
        思路：分三步，找到中间节点，反转后半边链表，循环比较
        """
        if not head or not head.next:
            return True
        pre = quick = slow = ListNode(0)
        pre.next = head
        #找到中间节点
        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next
        #反转右半边链表
        right = slow.next
        slow.next = None
        while right:
            tmp = right
            right = right.next
            tmp.next = slow.next
            slow.next = tmp
        #循环比较
        right = slow.next
        left = head
        while right:
            if left.val != right.val:
                return False
            right = right.next
            left = left.next
        return True
        
    def isHasCycle(self, head):
        """
        判断单链表是否有环
        :type head:ListNode
        :rtype:bool
        思路：快慢指针的一个典型应用，如果有环，快指针一定会和慢指针在环里相遇
        """
        fast = slow = ListNode(-1)
        fast.next = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def LinkListCycle(self, head):
        """
        判断单链表是否有环，有环的话找到环入口点
        :type head: ListNode
        :rtype : ListNode
        思路：快慢指针相遇之时，2(a + b) = a + n(b+c) + b ==> (n-1)(b+c) + c = a
        可知，相遇之时，把快指针移动到头结点pre,在快慢指针以相同的速度移动他们就会相遇在环的入口
        """
        pre = fast = slow = ListNode(-1)
        pre.next = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = pre
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None

    def getIntersectionNode(self, headA, headB):
        """
        判断两个链表(非带环)是否相交，如果相交，返回相交的首节点
        :type headA: ListNode
        :type headB: ListNode
        :rtype :ListNode
        思路:判断两个链表的长度，更长的链表先走(长度差)步，然后两个链表同速一起走，第一个相等的节点就是目标返回节点
        """
        pre_a = ListNode(-1)
        pre_b = ListNode(-1)
        pre_a.next = headA
        pre_b.next = headB
        length_a = length_b = 0
        while headA:
            length_a += 1
            headA = headA.next
        while headB:
            length_b += 1
            headB = headB.next
        if length_a < length_b:
            while length_b - length_a:
                headB = headB.next
                length_b -= 1
        else:
            while length_a - length_b:
                headA = headA.next
                length_a -= 1
        headA = pre_a
        headB = pre_b
        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
    
    def intersectionII(self, headA, headB):
        """
        扩展:判断带环链表是否相交
        :type headA: ListNode
        :type headB: ListNode
        :rtype: bool
        思路：带环链表，对于两链表相交，则环上的任意一个节点必然是另一个链表的节点，先快慢指针找到环上的某个节点，判断是否在另一个链表上
        """
        fast = slow = pre_a = ListNode(-1)
        pre_a.next = headA
        pre_b = ListNode(-1)
        pre_b.next = headB
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break        
        while headB:
            if headB == slow:
                return True
            else:
                headB = headB.next
        return False
      
if __name__ == '__main__':
    """
    l = LinkList()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print l.isPalindrome(head)
    """
    l = LinkList()
    head_a = ListNode(0)
    head_a.next = ListNode(1)
    head_a.next.next = ListNode(2)
    head_a.next.next.next = ListNode(3)
    head_a.next.next.next.next = ListNode(4)
    head_a.next.next.next.next.next = head_a.next.next
    head_b = ListNode(5)
    print l.intersectionII(head_a, head_b)
