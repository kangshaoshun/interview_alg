#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def countSegment(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s.strip():
            return 0
        return len([item for item in s.strip().split(' ') if item.strip()])
