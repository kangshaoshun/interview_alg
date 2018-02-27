#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s:str
        :rtype:bool
        Time Complexity:O(N)
        Space Complexity:O(1)
        """
        length = len(s)
        for i in range(1, length/2 + 1):
            if length % i:
                continue
            else:
                if s[:i] * (length / i) == s:
                    return True
        return False

if __name__ == '__main__':
    s = Solution()
    print s.repeatedSubstringPattern('abcabcabcabc')
