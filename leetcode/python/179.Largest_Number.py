#coding:utf-8
import sys
import random
reload(sys)
sys.setdefaultencoding('utf-8')
"""
    题意：构造最大的数
        eg. [3, 30, 34, 5, 9]   ==> 9534330
"""
def getRandomNumber(num):
    res = []
    for i in range(num):
        res.append(random.randint(0, 100))
    return res

class Solution:
    def largestNumber(self, nums):
        """
            Time Complexity:O(nlogn)
            Space Complexity:O(1)
        """
        nums = map(str, nums)
        nums.sort(cmp=lambda a, b:1 if a+b>b+a else -1 if a+b<b+a else 0, reverse=True)
        return str(int(''.join(nums)))

if __name__ == '__main__':
    s = Solution()
    nums = getRandomNumber(10)
    print s.largestNumber(nums)
