#coding:utf-8
"""
    Reverse String
"""

#I:
"""
    第一题很简单：直接反转一个字符串s
"""
class Solution(object):
    def reverse(self, s):
        return s[::-1]


#II
"""
    第二题，给定一个字符串s,以及常数k，每2k个字符反转前k个字符一次
    eg, s='abcdefg',k=2  r = 'bacdfeg'
"""
class Solution(object):
    def reverse(self, s, k):
        s = list(s)
        for i in xrange(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)

#III
"""
    第三题，感觉比第二题简单，s是一句话，包含多个字符串，现在将这句话的顺序不变，这是每个字符串反转
    s = 'kang shao shun' r = 'gnak oahs nuhs'
"""
class Solution(object):
    def reverse(self, s):
        s = s.split(' ')
        for i, item in enumerate(s):
            s[i] = ''.join(reversed(item))
        return ' '.join(s)
