#coding:utf-8
class Solution(object):
    def rotate(self, nums, k):
        """
            eg:
                inptut: nums:[1,2,3,4,5,6,7] k=3
                output: nums:[5,6,7,1,2,3,4,5]
        """
        if not k or k < 0:
            return
        length = len(nums)
        tmp_array = [i for i in nums[length-k:]]
        for i in range(length-k-1,-1,-1):
            nums[i+k] = nums[i]
        nums[:k] = tmp_array
        print nums


if __name__ == '__main__':
    s = Solution()
    nums = [1,2]
    s.rotate(nums, 1)
