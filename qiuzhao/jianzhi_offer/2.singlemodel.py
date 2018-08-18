#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
设计一个单例模式
单例模式是一个只能实例化一次的类
"""

class SingleMode(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingleMode, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(SingleMode):
    def __init__(self):
        self.val = 10

    def get_num(self):
        self.val += 1
        print self.val

if __name__ == '__main__':
    mc1 = MyClass()
    mc2 = MyClass()
    mc1.get_num()
    mc1.get_num()
    mc2.get_num()
