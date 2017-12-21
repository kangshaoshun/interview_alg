#coding:utf-8
"""
    题意：给定一个二进制字符串(只包含0 1)，计算连续的 count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

"""

class Solution(object):
    def countBinarySubstrings(self, s):
        """
            type s:str
            rtype: int
        """
        s = map(len, s.replace('01', '0 1').replace('10', '1 0').split(' '))
        return sum(min(a, b) for a, b in zip(s, s[1:]))

if __name__ == '__main__':
    s = Solution()
    print s.countBinarySubstrings('1110000')

