#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
从尾至头打印链表
"""

class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse_print_linklist(self, root):
        """
        从尾至头打印，很自然的想到栈的特性；而递归其实也是栈，所以可以考虑从这方面入手
        """
        #递归
        """
        if root:
            if root.next:
                self.reverse_print_linklist(root.next)
            print root.val
        """

        #栈
        stack = []
        while root:
            stack.append(root.val)
            root = root.next
        while stack:
            print stack.pop()


if __name__ == '__main__':
    root = LinkNode(1)
    root.next = LinkNode(2)
    root.next.next = LinkNode(3)
    root.next.next.next = LinkNode(4)
    s = Solution()
    s.reverse_print_linklist(root)

