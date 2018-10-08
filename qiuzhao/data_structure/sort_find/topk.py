#coding:utf-8
import sys
import random
reload(sys)
sys.setdefaultencoding('utf-8')

"""
所有关于topk的问题
"""

class Solution(object):
    def partition(self, nums, start, end):
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

    def get_ans(self, nums, start, end, k):
        index = self.partition(nums, start, end)
        while index != k - 1:
            if index < k - 1:
                index = self.partition(nums, index + 1, end)
            else:
                index = self.partition(nums, start, index - 1)
        return index

    def topK(self, nums, k):
        if not nums or k > len(nums) or k <= 0:
            return -1
        res = self.get_ans(nums, 0, len(nums) - 1, k)
        return nums[res]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 4, 5, 9, 1, 2, 3, 0, 2]
    print sorted(nums)
    print s.topK(nums, int(sys.argv[1]))
