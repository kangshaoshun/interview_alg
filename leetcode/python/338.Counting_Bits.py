#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def countBits(self, num):
        """
        :type num:int
        :rtype: List[int]
        """
        """
            Given a non negative integer number num.For every numbers i in the range 0<=i<=num calculate the number of 1's in their binary representation and return them as an array.
            Follow up:complete it with O(n) time complexity
            思路：没有follow up的话这题非常简单，就不写了，这里给出follow up的思路，要在O(n)的时间复杂度内完成这个工作，可见是存在一定规律的，res[i] = res[i & (i-1)] + 1, i 的1个数等于 i & (i-1)的1的个数 + 1
        """
        res = [0] * (num + 1)
        for i in range(num + 1):
            res[i] = res[i & (i-1)] + 1
        return res
