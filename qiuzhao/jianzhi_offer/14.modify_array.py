#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
调整数组的顺序，使得奇数总是位于偶数前面
"""

#考虑可扩展性
def is_odd(value):
    return value & 1

def modify_array(nums):
    if not nums:return
    length = len(nums)
    i, j = 0, length - 1
    while i < j:
        while nums[i] & 1:
            i += 1
        while not nums[j] & 1:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    return nums

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print modify_array(nums)
