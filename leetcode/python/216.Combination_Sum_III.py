#coding:utf-8
"""
    题意：排列组合，k个数的组合之和为n，k个数任意不重复
"""
from itertools import combinations
class Solution(object):
    def combinationSum3(self, k, n):
        """
            这里有一种吊炸天的解法，直接调用itertools中的排列组合库
        """
        return [c for c in combinations(range(1, 10), k) if sum(c)==n]


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum3(3, 9)

