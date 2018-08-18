#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
This script overall common alg in interview;
"""

class SortFind(object):
    """
    排序查找类相关算法
        冒泡排序
        选择排序
        归并排序
        快速排序
        堆排序
        计数排序
        桶排序
        二分查找
        topk
    """
    def bubbleSort(self, nums):
        """冒泡排序
        T = O(N^2)
        S = O(1)
        """
        length = len(nums)
        for i in range(length):
            for j in range(0, length - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
    
    def selectSort(self, nums):
        """选择排序
        T = O(N^2) 
        S = O(1)
        """
        length = len(nums)
        for i in range(length):
            tmp_index = i
            tmp_value = nums[i]
            for j in range(i + 1, length):
                if nums[j] < tmp_value:
                    tmp_value = nums[j]
                    tmp_index = j
            nums[i], nums[tmp_index] = nums[tmp_index], nums[i]
        return nums

    def mergeSort(self, nums):
        """归并排序
        采用分治策略：将数组无穷一分为二直至长度小于等于1. 对左右数组进行合并
        T = O(nlogn)
        S = O(n)
        """
        def merge(left, right):
            res = []
            while left and right:
                if left[0] <= right[0]:
                    res.append(left.pop(0))
                else:
                    res.append(right.pop(0))
            if left:res.extend(left)
            if right:res.extend(right)
            return res
        length = len(nums)
        if length <= 1:
            return nums
        mid = length >> 1
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return merge(left, right)

    def quickSort(self, nums):
        """快排 面试最常问的算法之一
        T = O(nlogn)
        S = O(1)
        """
        def qsort(nums, left, right):
            if left >= right:
                return
            i, j = left, right
            base = nums[i]
            while i < j:
                while i < j and nums[j] >= base:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= base:
                    i += 1
                nums[j] = nums[i]
            nums[i] = base
            qsort(nums, left, i - 1)
            qsort(nums, i + 1, right)
        qsort(nums, 0, len(nums) - 1)
        return nums

    def heapSort(self, nums):
        """堆排序
        
        """



class TreeTraversal(object):
    """
    二叉树遍历相关算法
    """
    pass


class LinkListAlg(object):
    """
    链表相关算法
    """
    pass


class DynamicProgramAlg(object):
    """
    动态规划相关算法
    """
    pass


class DBfsAlg(object):
    """
    DFS/BFS 相关算法
    """
    pass



if __name__ == '__main__':
    sf = SortFind()
    print sf.quickSort(eval(sys.argv[1]))
