#coding:utf-8
class Node(object):
    __slots__ = ['_value', '_next']
    def __init__(self, item):
        self._value = item
        self._next = None

    def getValue(self):
        return self._value

    def getNext(self):
        return self._next

    def setValue(self, value):
        self._value = value

    def setNext(self, newnext):
        self._next = newnext


#单链表的操作
"""
    1.初始化

    #插入
    2.在头部插入节点
    3.在尾部追加节点
    4.在指定index下插入节点

    #删除
    5.删除头节点
    6.删除尾节点
    7.删除指定index的节点 

    8.遍历单链表
    9.查找第index个节点（按坐标查找）
    10.查找value节点(按值查找)
"""
class LinkList(object):
    def __init__(self):
        self._head = None
    
    def isEmpty(self):
        return self_head == None

    def size(self):
        current = self._head
        length = 0
        while current != None:
            current = current.getNext()
            length += 1
        return length

    def add(self, value):
        tmp = Node(value)
        tmp.setNext(self._head)
        self._head = tmp

    def append(self, value):
        tmp = Node(value)
        if isEmpty():
            self._head = tmp
        else:
            current = self._head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(tmp)

    def insert(self, index, value):
        if index <= 1:
            self.add(value)
        elif index > self.size():
            self.append(value)
        else:
            current = self._head
            cnt = 1
            while cnt != index-1:
                cnt += 1
                current = current.getNext()
            tmp = Node(value)
            right = current.getNext()
            current.setNext(tmp)
            tmp.setNext(right)




if __name__ == '__main__':
    l = LinkList()
