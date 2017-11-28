#coding:utf-8
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
            思路：判断单链表是否有循环是快慢指针的一个典型应用，做法是慢指针每次移动一步，快指针每次移动多步（2），如果快指针到达链表尾端，则返回false,如果快指针和慢指针相遇了，则返回true
            Time Complexity:O(N)
        """
        if not head or not head.next:
            return False
        slow = head.next 
        fast = head.next.next
        while fast and fast.next:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False




if __name__ == '__main__':
    s = Solution()
