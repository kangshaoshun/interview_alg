#coding:utf-8
"""
    给定一个字符串s，和一个字典d，查出字典中可以通过字符串s删除字符得到的最长的字符串
"""
class Solution(object):
    def findLongestWord(self, s, d):
        """
            Time Complexity:O(M*N)
            Space Complexity:O(M)
        """
        def isSubsequence(x):
            it = iter(s)    #将字符串变成只可迭代一次的对象
            return all(c in it for c in x)
        return max(sorted(filter(isSubsequence, d)), key=len)


   def findLongestWord2(self, s, d):
        """
            no need sort. more efficient
        """
        def isSubsequence(x):
            it = iter(s)
            return all(c in it for c in x)
        return min(filter(isSubsequence, d), key=lambda x:(-len(x), x))






