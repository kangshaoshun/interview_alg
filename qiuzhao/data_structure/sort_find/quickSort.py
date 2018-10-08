#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class quickSort(object):
    def __init__(self):
        pass

    def partition(self, nums, start, end):
        if start <= end:
            i, j = start, end
            base = nums[start]
            while i < j:
                while i < j and nums[j] >= base:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= base:
                    i += 1
                nums[j] = nums[i]
            nums[i] = base
            return i

    def quickSort(self, nums, start, end):
        if start >= end:return
        index = self.partition(nums, start, end)
        if index > start:
            self.quickSort(nums, start, index - 1)
        if index < end:
            self.quickSort(nums, index + 1, end)
        return nums
    
    def topK(self, nums, start, end, k):
        if k < 1 or k > len(nums):return
        index = self.partition(nums, start, end)
        print nums
        print index
        if index + 1 == k:
             return nums[index]
        elif index + 1 < k:
            return self.topK(nums, index + 1, end, k)
        else:
            return self.topK(nums, start, index - 1, k)


if __name__ == '__main__':
    q = quickSort()
    nums = [1, 4, 2, 3, 5, 7, 8, 9, 6]
    #print 'origin', nums
    print q.quickSort(nums, 0, len(nums) - 1)
    print nums
    print q.topK(nums, 0, len(nums) - 1, int(sys.argv[1]))

