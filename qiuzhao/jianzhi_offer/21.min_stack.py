#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Stack(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)
        if not self.stack2:
            self.stack2.append(node)
        else:
            if node < self.stack2[-1]:
                self.stack2.append(node)

    def pop(self):
        if self.stack1:
            res = self.stack1.pop()
            if res == self.stack2[-1]:
                self.stack2.pop()
            return res
        else:
            raise Exception('no data')

    def top(self):
        if self.stack1:
            return self.stack1[-1]
        else:
            raise Exception('no data')

    def getMin(self):
        if self.stack2:
            return self.stack2[-1]
        else:
            raise Exception('no data')
