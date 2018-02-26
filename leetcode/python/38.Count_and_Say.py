#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
1
11
21
1211
111221
312211
13112221
1113213211
31131211131221
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n:int
        :rtype: str
        """
        res = '1'
        for _ in range(n-1):
            res = self.helper(res)
        print res

    def helper(self, s):
        pre = None
        cnt = 0
        res = ''
        for item in s:
            if not pre:
                pre = item
                cnt = 1
            else:
                if item == pre:
                    cnt += 1
                else:
                    res = res + str(cnt) + pre
                    pre = item
                    cnt = 1
        res = res + str(cnt) + pre
        return res

if __name__ == '__main__':
    s = Solution()
    s.countAndSay(5)
