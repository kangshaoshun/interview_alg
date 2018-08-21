#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
斐波那契数列
"""
def fib(n):
    if n == 0:return 0
    if n == 1:return 1
    fir, sec = 0, 1
    for _ in range(2, n + 1):
        sec, fir = fir + sec, sec
    return sec

if __name__ == '__main__':
    print fib(int(sys.argv[1]))
