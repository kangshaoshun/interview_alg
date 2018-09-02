#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
数字在排序数组中出现的次数

思路：
    用两个二分法查找左右的边界坐标
    返回坐标的差值就是重复元素的个数；

"""
class Solution(object):
    def getBorderIndex(self, nums, target, right=False):
        if not nums:return -1
        i, j = 0, len(nums) - 1
        mid = i + (j - i) / 2
        while i <= j:
            if nums[mid] == target:
                if not right:
                    #这里注意边界条件的判断，mid - 1 and mid + 1会越界
                    if mid - 1 <= 0 or nums[mid - 1] != target:
                        return mid
                    else:
                        j = mid - 1
                else:
                    if mid + 1 >= len(nums) or nums[mid + 1] != target:
                        return mid
                    else:
                        i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
            mid = i + (j - i) / 2
        return -1

    def binarySearch(self, nums, target):
        if not nums:
            return 0
        left = self.getBorderIndex(nums, target)
        right = self.getBorderIndex(nums, target, right=True)
        if left == right and left != -1:
            return 1
        return right - left + 1
        #print left, right


if __name__ == '__main__':
    s = Solution()
    print s.binarySearch(eval(sys.argv[1]), int(sys.argv[2]))



