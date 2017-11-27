#coding:utf-8
class Solution(object):
    def checkPossibility(self, nums):
        """
            Time Complexity:O(nlgn)
            Space Complexity:O(n)
            解题思路：
                最多只能变换一个元素，则考虑当遇到第一个左边的数大于右边的数的时候，调整这两个数的顺序，如果这个时候的顺序就是排序之后的顺序，则返回true
        """
        length = len(nums)
        one = nums[:]
        two = nums[:]
        for i in xrange(length-1):
            if nums[i] > nums[i+1]:
                one[i] = nums[i+1]
                two[i+1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4]
    print s.checkPossibility(nums)
