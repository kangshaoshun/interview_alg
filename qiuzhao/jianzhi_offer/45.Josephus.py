#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
约瑟夫环问题
"""
class Solution(object):
    """
    动态规划解决约瑟夫问题
    状态转移方程:
    f(n, m) = 
        0                       n = 1
        (f(n - 1, m) + m) % n   n > 2

    f(n, m)表示n个点每次删除第m个点最终剩下的点；

    推导这个状态转移方程见剑指Offer,关键是一个映射和逆映射问题；
    """
    def get_last_val(self, n, m):
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2, n + 1):
            last = (last + m ) % i
        return last


if __name__ == '__main__':
    s = Solution()
    print s.get_last_val(5, 3)

