#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
关于设计模式的种种
"""

class SingleModel(object):
    __one = None
    def __new__(cls, *args, **kwargs):
        if not cls.__one:
            cls.__one = super(SingleModel, cls).__new__(cls, *args, **kwargs)
        return cls.__one

class NeedToInstance(object):
    def __init__(self):
        pass

class FactoryMode(object):
    def __init__(self):
        super(FactoryMode, self).__init__()
        self.cls = NeedToInstance

    def get_instance(self):
        return self.cls()
    

if __name__ == '__main__':
    id1 = id(SingleModel())
    id2 = id(SingleModel())
    print id1 == id2

    #fm = FactoryMode()
    #print fm.get_instance().__class__.__name__
