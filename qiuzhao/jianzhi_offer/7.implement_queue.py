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


"""
引申：用两个队列实现一个栈
"""
class Stack(object):
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, val):
        if not self.queue1:
            self.queue2.append(val)
        else:
            self.queue1.append(val)

    def pop(self):
        if self.queue1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)
        else:
            if self.queue2:
                while len(self.queue2) > 1:
                    self.queue1.append(self.queue2.pop(0))
                return self.queue2.pop(0)
            else:
                raise Exception('No data to pop')

    def top(self):
        if self.queue1:
            return self.queue1[-1]
        elif self.queue2:
            return self.queue2[-1]
        else:
            raise Exception('no data')

    def empty(self):
        return not self.queue1 and not self.queue2


