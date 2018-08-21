#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
判断一个树是不是另一颗树的子结构
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSametree(self, root1, root2):
        if not root1 and not root2:return True
        if not root1 or not root2:return False
        if root1.val == root2.val:
            return self.isSametree(root1.left, root2.left) and self.isSametree(root1.right, root2.right)
        else:
            return False

    def isSubtree(self, root1, root2):
        result = False
        if root1 and root2:
            if root1.val == root2.val:
                result = self.isSametree(root1, root2)
            if not result:
                result = self.isSubtree(root1.left, root2)
            if not result:
                result = self.isSubtree(root1.right, root2)
        return result


if __name__ == '__main__':
    root1 = ListNode(3)
    root1.left = ListNode(4)
    root1.right = ListNode(5)
    root1.left.left = ListNode(1)
    root1.left.right = ListNode(2)
    #root1.left.right.left = ListNode(0)
    root2 = ListNode(4)
    root2.left = ListNode(1)
    root2.right = ListNode(2)
    s = Solution()
    print s.isSubtree(root1, root2)
