#coding:utf-8
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
            type l1:ListNode
            type l2:ListNode
            rtype: ListNode
        """
        """
            Time Complexity:O(N)
            Space Complexity:O(N)
            思路分析：借助辅助空间，将数字进行反转计算，然后将结果反转输出
        """
        n1 = []
        n2 = []
        while l1:
            n1.append(str(l1.val))
            l1 = l1.next
        while l2:
            n2.append(str(l1.val))
            l2 = l2.next
        res = int(''.join(n1[::-1])) + int(''.join(n2[::-1]))
        helper = ListNode(0)
        tmp = helper
        for item in str(res)[::-1]:
            tmp.next = ListNode(int(item))
            tmp = tmp.next
        return helper.next

