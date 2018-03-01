#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def square(x):
    """Calculates the square of the number x """
    return x * x

def changeName(n):
    n[0] = "Mr. XuHoo"


names = ['kang', 'shao', 'shun']
n = names[::]
changeName(n)
print names

