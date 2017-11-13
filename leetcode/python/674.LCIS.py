#coding:utf-8

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums:List[int]
        :rtype int
        """
        if not nums:
            return 0
        length = 1
        max_length = 1
        last = nums[0]
        for item in nums:
            if item > last:
                length += 1
                if length > max_length:
                    max_length = length
            else:
                length = 1
            last = item
        return max_length


if __name__ == "__main__":
    s = Solution()
    print s.findLengthOfLCIS([1,2,3,4,5])
