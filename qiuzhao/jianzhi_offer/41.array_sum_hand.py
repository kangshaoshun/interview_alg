#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
和为S 的正整数数组序列

和为S的两个数
"""
class Solution(object):
    def get_array_sum_hand(self, target):
        """
        :type target:int
        :rtype:List[List]
        """
        if target <= 2:
            return []
        nums = list(range(1, (target >> 1) + 2))
        print nums
        i, j = 0, 0
        res = nums[0]
        result = []
        while j < len(nums):
            while res < target:
                j += 1
                if j >= len(nums):
                    break
                res += nums[j]
            if res == target:
                result.append(nums[i:j+1])
                res -= nums[i]
                i += 1
            while res > target:
                res -= nums[i]
                i += 1
        return result

    def get_array_sum_two(self, nums, target):
        if not nums:return []
        length = len(nums)
        if length <= 1:return []
        i, j = 0, length - 1
        res = []
        while i < j:
            if nums[i] + nums[j] == target:
                res.append([nums[i], nums[j]])
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return res
        

if __name__ == '__main__':
    s = Solution()
    #print s.get_array_sum_hand(int(sys.argv[1]))
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    print s.get_array_sum_two(nums, 21)
