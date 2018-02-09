#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
7-0 7-1 6-2 5-3 5-4 4-5
7 7 6 5 5 4
0 1 1 0 2 4
0 1 2 3 4 5
5 7 6 7 5
"""
class Solution(object):
    def reconstruct(self, nums):
        """
        :type nums:List[List[int]]
        :rtype:List[List[int]]
        """
        """
            Time Complexity:O(N^2)
            Space Complexity:O(1)
        """
        nums.sort(key=lambda x:(x[0], -x[1]), reverse=True)
        for index, item in enumerate(nums):
            while index > item[1]:
                nums[index] = nums[index - 1]
                index -= 1
            nums[item[1]] = item
        return nums

if __name__ == '__main__':
    s = Solution()
    nums = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print s.reconstruct(nums)



