#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
最长回文子串

状态转移方程：
dp[i][j] = 
    1                                   j == i
    s[i] == s[j]                        j = i + 1
    s[i]==s[j] and dp[i + 1][j - 1]     j > i + 1

计算dp[i][j]为True时，j ,i 下标差的最大值就是最长回文子串
"""
