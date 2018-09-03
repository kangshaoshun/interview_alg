#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
两个二叉树节点的最低公共祖先
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def get_lca_node(self, root, p, q):
        if not root:return None
        stack = [(root, [])]
        res = []
        while stack:
            node, path = stack.pop()
            if (node.val == p.val) or (node.val == q.val):
                res.append(path)
            if node.right:
                tmp = path[:]
                tmp.append("right")
                stack.append((node.right, tmp))
            if node.left:
                tmp = path[:]
                tmp.append('left')
                stack.append((node.left, tmp))
            print stack
            print res
        print res
        ret = root
        for val1, val2 in zip(res[0], res[1]):
            if val1 == val2:
                if val1 == 'left':
                    ret = ret.left
                else:
                    ret = ret.right
            else:
                return ret
        return ret

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    b = root.left.right.left = TreeNode(8)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.left.right = TreeNode(9)
    a = root.right.left.right.right = TreeNode(11)
    root.right.right.left = TreeNode(10)
    s = Solution()
    print a, b
    print s.get_lca_node(root, a, b).val
