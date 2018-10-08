#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
编辑距离

状态转移方程
dp[i][j] = 
    dp[i - 1][j - 1]                                            s[i] == s[j]
    max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1       s[i] != s[j]

    分别对应 删除   增加    修改 的三种情况
"""


