#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
逆序对 的个数
"""

class Solution(object):
    def __init__(self):
        self.reverse_num = 0

    def mergeSort(self, nums):
        length = len(nums)
        if length <= 1:
            return nums
        def merge(nums1, nums2):
            print nums1, nums2
            result = []
            i, j = 0, 0
            length_1, length_2 = len(nums1), len(nums2)
            while i < length_1  and j < length_2:
                if nums1[i] <= nums2[j]:
                    result.append(nums1[i])
                    i += 1
                else:
                    self.reverse_num += (length_1 - i)
                    print "small:",nums1[i]
                    result.append(nums2[j])
                    j += 1
            if i == length_1:
                result.extend(nums2[j:])
            if j == length_2:
                result.extend(nums1[i:])
            return result
        mid = length >> 1
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return merge(left, right)



if __name__ == '__main__':
    s = Solution()
    print s.mergeSort(eval(sys.argv[1]))
    print s.reverse_num

