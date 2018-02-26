#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :type: bool
        Time Complexity:O(N)
        Space Complexity:O(N)
        """
        left = []
        right = []
        for c in s:
            if c.isalnum():
                left.append(c.lower())
        for c in s[::-1]:
            if c.isalnum():
                right.append(c.lower())
        return left == right
