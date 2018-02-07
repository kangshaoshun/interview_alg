#coding:utf-8
import sys
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def findAnagrams(self, s, p):
        """
            Time Complexity:O(N)        
            Space Complexity:O(1)
            思路：滑动窗口，与哈希值的结合使用，注意下标，下标不方便确定可以用几个例子演示一遍即可
        """
        res = []
        m, n = len(p), len(s)
        if m > n:
            return res
        s_hash = [0] * 123
        p_hash = [0] * 123
        for item in p:
            p_hash[ord(item)] += 1
        for item in s[:m]:
            s_hash[ord(item)] += 1
        for i in range(n-m+1):
            if s_hash == p_hash:
                res.append(i)
            s_hash[ord(s[i])] -= 1
            if i + m >= n:
                continue
            s_hash[ord(s[i + m])] += 1
        return res

if __name__ == '__main__':
    so = Solution()
    s = 'cbaebabacd'
    p = 'abc'
    print so.findAnagrams(s, p)
