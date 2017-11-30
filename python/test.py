#coding:utf-8
from stack import Stack

def test(string):
    s = Stack()
    for item in string:
        if item == '(':
            s.push(item)
        elif item == ')' and not s.isEmpty():
            s.pop()
        else:
            return False
    return True


if __name__ == '__main__':
    print test('((((()))))')
