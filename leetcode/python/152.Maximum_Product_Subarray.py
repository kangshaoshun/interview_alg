#coding:utf-8

class Solution(object):
    def maxProduct(self, nums):
        if len(nums) == 1:
            return nums[0]
        product = 1
        max_product = 0
        minus_item = 0
        for item in nums:
            if item < 0:
                minus_item = item
                product *= item
                if product > max_product:
                    max_product = product
            elif item == 0:
                product = 1
            else:
                product *= item
                if product > max_product:
                    max_product = product
        return max_product


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 3, -2, -4]
    print s.maxProduct(nums)
