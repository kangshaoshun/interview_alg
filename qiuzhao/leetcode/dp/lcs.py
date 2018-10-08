#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
最长公共子串

动态规划思路：

s[i][j] = 
    s[i- 1][j - 1] + 1                  s[i] == s[j]
    max(s[i - 1][j], s[i][j - 1])       s[i] != s[j]
"""

class Solution(object):
    def lcs(self, nums1, nums2):
        if not nums1 or not nums2:
            return 0
        m, n = len(nums1), len(nums2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        print dp
        for i in range(n):
            dp[0][i] = 0
        for i in range(m):
            dp[i][0] = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        print dp
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    nums1 = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    nums2 = ['B', 'D', 'C', 'A', 'B', 'A']
    print s.lcs(nums1, nums2)
