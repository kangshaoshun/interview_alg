#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
合并两个排序的链表
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeLinklist(self, link1, link2):
        if not link1 and not link2:return None
        if not link1:return link2
        if not link2:return link1
        if link1.val <= link2.val:
            head = link1
            link1 = link1.next
        else:
            head = link2
            link2 = link2.next
        res = head
        while link1 and link2:
            if link1.val <= link2.val:
                head.next = link1
                link1 = link1.next
            else:
                head.next = link2
                link2 = link2.next
            head = head.next
        if link1:
            head.next = link1
        if link2:
            head.next = link2
        return res
        

            

