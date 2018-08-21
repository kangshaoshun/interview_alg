#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
位运算
"""
def get_bitnum(n):
    cnt = 0
    while n:
        n = n & (n - 1)
        cnt += 1
    return cnt


if __name__ == '__main__':
    print get_bitnum(7)
