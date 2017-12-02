#coding:utf-8
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
            type l1: ListNode
            type l2: ListNode
            rtype: ListNonde
        """
        """
            题意:用单链表表示的两个整数，求相加后的和，返回类型是单链表
            eg. 7 -> 2 -> 4 -> 3  + 5 -> 6 -> 4
            output: 7 -> 8 -> 0 -> 7

            Time Complexity:O(N)
            Space Complexity:O(N)
        """
        if not l1 or not l2:
            return l1 if l1 else l2
        n1_str = []
        n2_str = []
        while l1:
            n1_str.append(str(l1.val))
            l1 = l1.next
        while l2:
            n2_str.append(str(l2.val))
            l2 = l2.next
        n1 = int("".join(n1_str))
        n2 = int("".join(n2_str))
        res = n1 + n2
        head = ListNode(0)
        ret = head
        for item in str(res):
            tmp = ListNode(int(item))
            head.next = tmp
            head = head.next
        return ret.next


if __name__ == '__main__':
    head = ListNode(7)
    head1 = head
    head.next = ListNode(2)
    head = head.next
    head.next = ListNode(4)
    head = head.next
    head.next = ListNode(3)

    head_2 = ListNode(5)
    head2 = head_2
    head_2.next = ListNode(6)
    head_2 = head_2.next
    head_2.next = ListNode(4)
    s = Solution()
    ret = s.addTwoNumbers(head1, head2)
    while ret:
        print ret.val
        ret = ret.next


