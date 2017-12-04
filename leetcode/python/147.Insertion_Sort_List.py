#coding:utf-8
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
        题意：使用插入排序排序单链表
        思路：
            插入排序的思想
            大于end 排在后
            小于head 排在前
            介于中间 查找插入位置
            Time Complexity:O(N*N)
            Space Complexity:O(1)
    """
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        end = head
        tmp = end.next
        while tmp:
            if tmp.val >= end.val:
                end = tmp
            elif tmp.val <= head.val:
                end.next = tmp.next
                tmp.next = head
                head = tmp
                tmp = end
            else:
                head_t = head
                while head_t and head_t.next:
                    if head_t.val <= tmp.val and head_t.val >= tmp.val:
                        end.next = tmp.next
                        tmp.next = head_t.next
                        head_t.next = tmp
                        tmp = end
                        break
                    else:
                        head_t = head_t.next
            tmp = end.next
        return head
