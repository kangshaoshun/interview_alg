#coding:utf-8
class Solution(object):
    def deleteNode(self, node):
        """
            :type node:ListNode
            :rtype:void Do not return anything,modify node in-place
        """
        """
            这是一道面试中经常问的算法题，很简单，但是如果思路没打开就容易想不到，会局限在本科学数据结构链表删除操作中。
            删除单链表的某个节点，但是只给你访问这个节点的通道

            思路：将该节点的下一个节点复制过来，这样，当前节点就已经被下一个节点移动过来了，直接删除当前节点的下一个节点就ok了
        """
        node.val = node.next.val
        node.next = node.next.next

