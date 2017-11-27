#coding:utf-8
class Solution(object):
    def plusOne(self, nums):
        """
            这道题没什么技术难度，思路是从后往前，如果是9，则进位标识置位true,否则，加1返回即可
            Time Complexity:O(N)
            Space Complexity:O(1)
        """
        flag = False
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 9:
                nums[i] = 0
                flag = True
            else:
                nums[i] += 1
                return nums
        if flag:
            b = [1]
            b.extend(nums)
            return b
        



if __name__ == '__main__':
    a = [0]
    s = Solution()
    print s.plusOne(a)
