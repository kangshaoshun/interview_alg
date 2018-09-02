#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
数组中只出现一次的数字

思路：从数组中找出只出现一次的数字，如果只有一个数字只出现一次，直接异或就ok.

这道题有两个只出现一次的数字，需要从上面这道题中迁移过来。

数组全部异或，得到的是两个只出现一次的数字的异或，如果可以把这两个单独出现的数字分开来就好办了；

方案就是利用这个异或值，找到这个异或值最右位为1的这位（其实只要是1的这位就可以），然后用这个1区分这两个只出现一次的数字
"""

class Solution(object):
    def getOneDigit(self, nums):
        """
        :type nums:List[int]
        :rtype: tuple
        """
        length = len(nums)
        if length <= 1:
            return nums
        tmp = 0
        for value in nums:
            tmp ^= value
        print tmp
        val = 1
        while tmp & val == 0:
            val = val << 1
        print val
        nums_left, nums_right = [], []
        for item in nums:
            if item & val:
                nums_left.append(item)
            else:
                nums_right.append(item)
        left, right = 0, 0
        for item in nums_left:
            left ^= item
        for item in nums_right:
            right ^= item
        print left, right
        return left, right

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 4, 2, 3, 1, 6]
    s.getOneDigit(nums)


