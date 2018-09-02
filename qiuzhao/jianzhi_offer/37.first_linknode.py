#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
找两个链表的第一个公共节点
"""

class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getFirstNode(object, root_a, root_b):
        if not root_a or not root_b:
            return None
        len_a, len_b = 0, 0
        tmp_a, tmp_b = root_a, root_b
        while tmp_a:
            tmp_a = tmp_a.next
            len_a += 1
        while tmp_b:
            tmp_b = tmp_b.next
            len_b += 1
        flag = False
        if len_a > len_b:
            len_diff = len_a - len_b
        else:
            len_diff = len_b - len_a
            flag = True
        if not flag:
            while len_diff:
                root_a = root_a.next
                len_diff -= 1
        else:
            root_b = root_b.next
            len_diff -= 1
        while root_a != root_b:
            root_a = root_a.next
            root_b = root_b.next
        return root_a


if __name__ == '__main__':
    s = Solution()
    tmp = LinkNode(-1)
    root_a = LinkNode(0)
    root_a.next = LinkNode(1)
    root_a.next.next = tmp
    root_b = LinkNode(2)
    root_b.next = LinkNode(3)
    root_b.next.next = LinkNode(4)
    root_b.next.next.next = tmp
    print s.getFirstNode(root_a, root_b).val
