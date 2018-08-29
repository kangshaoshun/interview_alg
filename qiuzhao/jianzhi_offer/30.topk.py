#coding:utf-8
import sys
import random
reload(sys)
sys.setdefaultencoding('utf-8')

def partition(nums, start, end):
    if start <= end:
        tmp = random.randint(start, end)
        base = nums[tmp]
        i, j = start, end
        nums[i], nums[tmp] = nums[tmp], nums[i]
        while i < j:
            while i < j and nums[j] >= base:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= base:
                i += 1
            nums[j] = nums[i]
        nums[i] = base
        return i

def topk(nums, k):
    if k < 0 or k > len(nums):
        return -1
    def get_result(nums, start, end, k):
        index = partition(start, end, k)
        while index + 1 != k:
            if index + 1 < k:
                index = partition(index + 1, end, k)
            else:
                index = partition(start, index - 1, k)
        return nums[index]

    return get_result(nums, 0, len(nums) - 1, k)
