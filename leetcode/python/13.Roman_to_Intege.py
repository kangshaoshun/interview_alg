#coding:utf-8
"""
    Convert Roman to Integer
"""
class Solution(object):
    """
        这只是一个简单的映射加一点逻辑
        逻辑就是：如果i位置的字符值比i+1位置的字符的值大，那么就累加，否则，减掉i位置字符的值
    """
    def romanToInt(self, s):
        roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        z = 0
        for i in range(0, len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]




if __name__ == '__main__':
    s = Solution()
    print s.romanToInt('MM')
