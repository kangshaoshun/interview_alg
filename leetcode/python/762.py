#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.
"""
class Solution(object):
    def isPrime(self, n):
        """
            判断一个整数是否是质数
        """
        if not n or n == 1:
            return False
        i = 2
        while i * i <= n:
            if not n % i:
                return False
            i += 1
        return True

    def countPrimeSetBits(self, L, R):
        cnt = 0
        for i in range(L, R + 1):
            if self.isPrime(bin(i).count('1')):
                cnt += 1
        return cnt
