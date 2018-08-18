#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (37.44%)
# Total Accepted:    207.7K
# Total Submissions: 554.6K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# 
# 
# Given an integer n, generate the nth term of the count-and-say sequence.
# 
# 
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# Example 1:
# 
# Input: 1
# Output: "1"
# 
# 
# 
# Example 2:
# 
# Input: 4
# Output: "1211"
# 
# 
#
class Solution(object):
    def count(self, s):
        res = []
        pre = ''
        cnt = 1
        for c in s:
            if not pre:
                pre = c
            elif c != pre:
                res.append(cnt)
                res.append(pre)
                pre = c
                cnt = 1
            else:
                cnt += 1
        res.append(cnt)
        res.append(pre)
        return ''.join(map(str, res))

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        """
        解题思路：采用递归的思路，注意边界 if n < 2 return '1';
        Time Complxity: O(n^2)
        """
        if n < 2:
            return '1'
        i = 2
        res = self.count(str(1))
        while i < n:
            res = self.count(res)
            i += 1
        return res
