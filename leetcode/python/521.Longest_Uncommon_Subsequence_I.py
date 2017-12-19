#coding:utf-8
"""
    题意：找出最长的非公共子序列，非公共子序列定义是：一个字符串的子序列，它不属于另一个字符串的字序列。突然觉得这道题有点傻,
"""
class Solution(object):
    def findLUSlength(self, a, b):
        return -1 if a==b else max(len(a), len(b))
