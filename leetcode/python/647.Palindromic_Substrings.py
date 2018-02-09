#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def countSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        def isPal(t):
            return t == ''.join(reversed(t))
        l = len(s)
        cnt = 0
        for i in range(l):
            for j in range(i, l+1):
                if not s[i:j]:
                    continue
                if isPal(s[i:j]):
                    print s[i:j]
                    cnt += 1
        return cnt
        """
        #参考discuss
        return sum(s[i:j] == s[i:j][::-1] for j in range(len(s) + 1) for i in range(j))

if __name__ == '__main__':
    s = Solution()
    ss = 'aba'
    print s.countSubstring(ss)
