#coding:utf-8
class Stack(object):
    """
        栈有几个功能：
            1.判断栈是否为空
            2.入栈
            3.出栈
            4.栈顶元素
    """
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception('stack empty')
        return self.items.pop()

    def top(self):
        if self.isEmpty():
            raise Exception('stack empty')
        return self.items[-1]
    
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print s.top()
    print s.pop()
    print s.pop()
    print s.isEmpty()
    print s.size()
    print s.pop()
    print s.size()
    print s.top()
