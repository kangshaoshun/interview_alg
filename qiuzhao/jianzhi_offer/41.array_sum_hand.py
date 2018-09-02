#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
和为S 的正整数数组序列
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

if __name__ == '__main__':
    s = Solution()
    print s.get_array_sum_hand(int(sys.argv[1]))
