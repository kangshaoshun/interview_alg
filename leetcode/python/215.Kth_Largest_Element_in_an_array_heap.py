#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def heapAdjust(self, nums, i, size):
        """
        :type nums:List[int]
        :rype i:int
        :type size:int
        """
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        max = i
        if i < size / 2:
            if lchild < size and nums[lchild] > nums[max]:
                max = lchild
            if rchild < size and nums[rchild] > nums[max]:
                max = rchild
            if max != i:
                nums[i], nums[max] = nums[max], nums[i]
                self.heapAdjust(nums, max, size)

    def buildHeap(self, nums):
        """
        :type nums:List[int]
        """
        size = len(nums)
        for i in range(size / 2 - 1, -1, -1):
            self.heapAdjust(nums, i, size)

    def heapSort(self, nums, k):
        """
        :type nums:List[int]
        :type k:int
        :rtype:int
        """
        self.buildHeap(nums)
        size = len(nums)
        j = 1
        for i in range(size - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            if j >= k:
                break
            self.heapAdjust(nums, 0, i)
            j += 1
        return nums[size - k]

    def findKthLargest(self, nums, k):
        """
        :type nums:List[int]
        :type k:int
        """
        return self.heapSort(nums, k)

if __name__ == '__main__':
    s = Solution()
    #nums = [1, 9, 2, 3, 0, 20, 10, 11, 17, 6, 8]
    #nums = [1]
    nums = [-1, 2, 0]
    print nums
    print s.findKthLargest(nums, 1)
    print nums


