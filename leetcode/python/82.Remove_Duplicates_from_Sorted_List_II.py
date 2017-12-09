#coding:utf-8
class ListNode(object):
    def __init__(self):
        self.val = x
        self.next = None

class Solution(object):
    """
        题意：删除单链表中的重复元素II,只要这个元素是重复元素，就删除，这是和I的区别。
    """
    def deleteDuplicates(self, head):
        """
            Time Complexity:O(N)
            Space Complexity:O(1)
        """
        dummy_node = ListNode(0)
        dummy_node.next = head
        pre = dummy_node
        while head and head.next:
            if head.val != head.next.val:
                pre.next = head
                pre = head
                head = head.next
            else:
                tmp = head.val
                while head and head.val == tmp:
                    head = head.next
        #这是至关重要的一步，很容易忘记，最后当head到达链表尾端的时候，记得要处理pre的next。
        pre.next = head
        return dummy_node

