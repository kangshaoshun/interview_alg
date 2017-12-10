#coding:utf-8
"""
    题意：判断两个字符串是否由颠倒字母顺序而构成的
    Time Complexity:O(max(length(s), length(t))
    Space Complexity:O(max(len(s), len(t)))
"""
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        #solution 1
        return Counter(s) == Counter(t)
        
        #solution 2
        return sorted(t) = sorted(s)

