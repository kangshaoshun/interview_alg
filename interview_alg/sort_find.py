#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
排序与查找 基础算法

排序：
    插入排序:直接插入排序，希尔排序

    选择排序：简单选择排序，堆排序

    交换排序：冒泡排序， 快速排序

    归并排序

    基数排序

查找
    
"""
class Solution(object):
    def insertSort(self, nums):
        """
        直接插入排序:一个一个插入，比val大的就往后挪 O(n^2)
        :type nums:List[int]
        :rtype :List[int]
        """
        length = len(nums)
        if length <= 1 :
            return nums
        for i in range(1, length):
            j = i - 1
            val = nums[i]
            while j >= 0 and nums[j] > val:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j+1] = val
        return nums

    def shellSort(self, nums):
        """
        希尔排序 插入排序的优化，间隔gap进行插入排序
        :type nums:List[int]
        :rtype:List[int]
        """
        length = len(nums)
        gap = length / 2
        while gap >= 1:   
            for j in range(gap, length):
                i = j
                while (i - gap) >= 0:
                    if nums[i] < nums[i - gap]:
                        nums[i], nums[i - gap] = nums[i - gap], nums[i]
                        i -= gap
                    else:
                        break
            gap /= 2
        return nums

    def simpleSelectSort(self, nums):
        """
        简单选择排序 选择一个剩余列表中的最大或最小值放到指定位置 O(N^2)
        :type nums:List[int]
        :rtype : List[int]
        """
        length = len(nums)
        if length <= 1:
            return nums
        for i in range(length):
            val = nums[i]
            index = i
            for j in range(i+1, length):
                if nums[j] < val:
                    val = nums[j]
                    index = j
            nums[i], nums[index] = nums[index], nums[i]
        return nums

    def build_heap(self, nums):
        size = len(nums)
        for i in range(size/2 - 1, -1, -1):
            self.adjust_heap(i, size, nums)
        return nums

    def adjust_heap(self, i, size, nums):
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
                self.adjust_heap(max, size, nums)

    def heapSort(self, nums):
        """
        堆排序 T = O(nlogn) S = O(1)
        :type nums:List[int]
        :rtype : List[int]
        """
        self.build_heap(nums)
        size = len(nums)
        for i in range(size - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.adjust_heap(0, i, nums)
        return nums

    def bubbleSort(self, nums, k):
        """
        冒泡排序
        :type nums:List[int]
        :rtype nums:List[int]
        """
        size = len(nums)
        for i in range(k):
            for j in range(size - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums[-k]

    def quickSort(self, nums, start, end):
        """
        快排：最常考的排序算法
        :type nums:List[int]
        :type start: int
        :type end:int
        :rtype:List[int]
        """
        if start < end:
            left, right = start, end
            base = nums[left]
            while left < right:
                while right > left and nums[right] >= base:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= base:
                    left += 1
                nums[right] = nums[left]
            nums[left] = base
            self.quickSort(nums, start, left - 1)
            self.quickSort(nums, left + 1, end)
        return nums
    
    def merge(self, left, right):
        """
        :type left:List[int]
        :type right:List[int]
        :rtype : List[int]
        """
        res = []
        i, j = 0, 0
        while left and right:
            if left[0] < right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        if left:
            res.extend(left)
        if right:
            res.extend(right)
        return res
        
    def mergeSort(self, nums):
        """
        归并排序 O(nlogn)
        :type nums:List[int]
        :rtype : List[int]
        """
        if len(nums) <= 1:
            return nums
        mid = len(nums) / 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left, right)

    #非比较类排序
    def radixSort(self, nums):
        """
        基数排序 T = O(N) S = O(N)
        :type nums:List[int]
        :rtype : List[int]
        """
        for k in xrange(len(str(max(nums)))):
            s = [[] for i in xrange(10)]
            for i in nums:
                s[i / (10**k) % 10].append(i)
            nums = [a for b in s for a in b]
        return nums
    
    def countSort(self, nums):
        """
        计数排序 T = O(N)
        计数排序的思想：对数据计数，统计该数应该放在最终的哪个位置，直接放置即可
        :type nums:List[int]
        :rtype:List[int]
        """
        size = len(nums)
        if size <= 1:
            return nums
        backup = [0 for i in xrange(size)]
        cnt = [0 for i in xrange(max(nums) + 1)]
        for i in nums:
            cnt[i] += 1
        for i in range(1, len(cnt)):
            cnt[i] = cnt[i - 1] + cnt[i]
        for i in nums:
            backup[cnt[i] - 1] = i
            cnt[i] -= 1
        return backup

    def binaryFind(self, nums, target):
        """
        二分查找 nums必须有序
        :type nums: List[int]
        :type target: int
        :rtype : int
        """
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

if __name__ == '__main__':
    nums = [1, 3, 8, 9, 10, 11, 13, 15]
    s = Solution()
    val = int(sys.argv[1])
    print s.binaryFind(nums, val)
