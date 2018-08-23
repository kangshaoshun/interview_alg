#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
判断栈的输出序列是否是输入序列的一种可能输出
"""

def isPopOrder(pushV, popV):
    if not pushV or not popV:
        return False
    stack = []
    for val in pushV:
        stack.append(val)
        while stack and stack[-1] == popV[0]:
            stack.pop()
            popV.pop(0)
    return False if stack else True
