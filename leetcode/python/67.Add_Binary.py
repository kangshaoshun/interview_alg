#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
Given two binary strings, return their sum (also a binary string).
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a:str
        :type b:str
        :rtype :str
        Time Complexity:O(N)
        Space Complexity:O(1)
        """
        res_a = res_b = 0
        for i, c in enumerate(a[::-1]):
            res_a = res_a + int(c) * (2 ** i)
        for i, c in enumerate(b[::-1]):
            res_b = res_b + int(c) * (2 ** i)
        return bin(res_a + res_b)[2:]
