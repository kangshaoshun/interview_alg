#coding:utf-8
"""
    原题链接：https://leetcode.com/problems/intersection-of-two-arrays/description/
    题意：找出两个列表的交集
    解题思路：转化成集合，然后取集合的交集
"""
class Solution(object):
    def intersection(self, nums1, nums2):
        """
            rtype:List[int]
        """
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print s.intersection(nums1, nums2)

