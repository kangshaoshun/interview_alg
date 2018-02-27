#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs:List[str]
        :rtype: str
        abcdefghi
        abcdef
        abcf
        abcdfe
        """
        if not strs:
            return ""
        s = min(strs, key=len)
        for i in range(len(s) + 1):
            if len(set([item[:i] for item in strs])) > 1:
                return s[:i-1]
        else:
            return s



if __name__ == '__main__':
    s = Solution()
    strs = ['abcdefghi', 'cbcdef', 'ebcdf', 'bcdfe']
    print s.longestCommonPrefix(strs)

