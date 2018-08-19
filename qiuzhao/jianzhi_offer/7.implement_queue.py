#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
用两个栈实现一个队列

"""

class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            if self.stack1:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
            else:
                raise Exception('no data')
