#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.
"""

class Solution(object):
    """
    :type s:str
    :rtype:int
    """
    return len(s.strip().split(' ')[-1])
