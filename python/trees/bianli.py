#coding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(root):
    """
        深度优先遍历
    """
    stack = [root]
    while stack:
        node = stack.pop()
        print node.val
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def bfs(root):
    """
        广度优先遍历
    """
    q = [root]
    while q:
        q1 = []
        while q:
            node = q.pop(0)
            print node.val
            if node.left:
                q1.append(node.left)
            if node.right:
                q1.append(node.right)
        q = q1
    
"""
    前序，中序，后序遍历（递归，非递归）
"""

# 递归实现
def preRecursion(root):
    """
        前序
    """
    if root:
        print root.val
        preRecursion(root.left)
        preRecursion(root.right)

def midRecursion(root):
    """
        中序
    """
    if root:    
        midRecursion(root.left)
        print root.val
        midRecursion(root.right)

def postRecursion(root):
    """
        后序
    """
    if root:
        postRecursion(root.left)
        postRecursion(root.right)
        print root.val
        
#非递归实现
def preNonRecursion(root):
    """
        前序
    """
    stack = []
    node = root 
    while node or stack:
        while node:
            stack.append(node)
            print node.val
            node = node.left
        if stack:
            node = stack.pop()
            node = node.right

def midNonRecursion(root):
    """
        中序
    """
    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        if stack:
            node = stack.pop()
            print node.val
            node = node.right


def postNonRecursion(root):
    """
        后序
    """
    stack = []
    node = root
    pre = None
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack[-1]
        if not node.right or node.right == pre:
            print node.val
            pre = node
            stack.pop()
            node = None
        else:
            node = node.right
            
            

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(7)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(5)
#    bfs(root)
    #preRecursion(root)
    #midRecursion(root)
    #postRecursion(root)
    #preNonRecursion(root)
#    midNonRecursion(root)
    postNonRecursion(root)
