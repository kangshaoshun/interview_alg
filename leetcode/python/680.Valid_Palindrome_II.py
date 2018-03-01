#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s:str
        :rtype:bool
        """
        return self.helper(s, 0, len(s) - 1, 0)

    def helper(self, s, start, end, delCnt):
        """
        Time Complexity:O(N)
        Space Complexity:O(1)
        """
        if delCnt > 1:
            return False
        while start < end:
            if s[start] != s[end]:
                break
            start += 1
            end -= 1
        if start == end or (start == end - 1):#(字符串个数为奇偶时的start和end的情况)
            return True
        return any([self.helper(s, start + 1, end, delCnt + 1), self.helper(s, start, end - 1, delCnt + 1)])

if __name__ == '__main__':
    s = Solution()
    print s.validPalindrome('abdca')
