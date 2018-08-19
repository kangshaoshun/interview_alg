#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
替换字符串的空格为'%20'
"""

class Solution(object):
    def replace_str(self, s):
        return s.replace(' ', '%20')

if __name__ == '__main__':
    s = Solution()
    t = 'We are happy'
    print s.replace_str(t)

