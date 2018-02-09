#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def productException(self, nums):
        """
        :type nums:List[int]
        :rtype:int
        """
        """
            不用除法解决这个问题，Time Complexity:O(N)
            思路：使用排山倒海法，从前往后乘一次，从后往前乘一次
        """
        left, right = [], []
        product = None
        for index, item in enumerate(nums):
            if not index:
                product = item
                left.append(1)
            else:
                left.append(product)
                product *= item
        product = None
        for index, item in enumerate(nums[::-1]):
            if not index:
                product = item
                right.append(1)
            else:
                right.append(product)
                product *= item
        res = []
        for x, y in zip(left, right):
            res.append(x * y)
        return res
