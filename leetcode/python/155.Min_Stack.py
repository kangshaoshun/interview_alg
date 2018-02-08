#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.value_stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x:int
        :rtype:void
        """
        self.value_stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype:int
        """
        val = self.value_stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        """
        rtype:int
        """
        return self.value_stack[-1]

    def getMin(self):
        """
        rtype:int
        """
        return self.min_stack[-1]



obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print obj.getMin()
print obj.pop()
print obj.top()
print obj.getMin()
