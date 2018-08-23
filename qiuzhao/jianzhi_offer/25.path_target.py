#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
求二叉树中的路径为某个值的路径
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = []

    def get_path(self, root, target):
        if not root:return 
        self.traversal([root, [root.val], root.val], target)
        self.result.sort(key=len, reverse=True)
        return self.result

    def traversal(self, node_list, target):
        node, path, res = node_list
        if not node.left and not node.right and res == target:
            self.result.append(path)
        if node.left:
            path_tmp = path[:]
            path_tmp.append(node.left.val)
            tmp = [node.left, path_tmp, res + node.left.val]
            self.traversal(tmp, target)
        if node.right:
            path_tmp = path[:]
            path_tmp.append(node.right.val)
            tmp = [node.right, path_tmp, res + node.right.val]
            self.traversal(tmp, target)

if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    s = Solution()
    print s.get_path(root, 22)
