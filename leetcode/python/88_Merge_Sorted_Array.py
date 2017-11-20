#coding:utf-8
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
            这道题是一道经典的题目，合并两个有序数组in-place.还有合并两个有序链表inplace，链表的简单点
            数组 nums1 长度m
            数组 nums2 长度n
            nums1长度足够，大于m+n
            解题思路：
                从后往前，将目前最大的放在目前的最后面
        """
        nums1.extend(nums2)
        while m>0 and n>0:
            if nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        if m == 0:
            nums1[:n] = nums2[:n]
        return nums1



if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 3, 4, 7, 9]
    nums2 = [2, 8, 10]
    print s.merge(nums1, len(nums1), nums2, len(nums2))



