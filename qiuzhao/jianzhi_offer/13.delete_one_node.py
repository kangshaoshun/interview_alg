#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
在O(1)时间删除单链表中的节点
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def delete_node(self, head, node):
        """
        思路：狸猫换太子
        但是如果结点是尾结点，依然需要O(N)
        只是平均时间复杂度是O(1)
        """
        if not head or not head.next:
            return None
        if not node.next:
            tmp = head
            while tmp.next != node:
                tmp = tmp.next
            tmp.next = None
            return head
        else:
            node.val = node.next.val
            node.next = node.next.next
            return head


