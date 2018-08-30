#coding:utf-8
import sys
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf-8')

"""
第一个只出现一次的字符
"""

class Solution(object):
    def get_first_once(self, s):
        if not s:return
        s_dict = Counter(s)
        for c in s:
            if s_dict[c] == 1:
                return c


if __name__ == '__main__':
    s = Solution()
    print s.get_first_once(sys.argv[1])


