#coding:utf-8

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        type nums:List[int]
        rtype: int
       """
        #SOLUTION ONE
        if not nums:
            return 1
        nums = list(set(nums))
        nums.sort()
        i = 1
        for item in nums:
            if item <= 0:
                continue
            elif item != i:
                return i
            else:
                i += 1
        return i

        #SOLUTION TWO 
        '''
            Time Complexity:O(N)
            Space Complexity:O(N)
        '''
        if not nums:
            return 1
        n = len(nums)
        d = {i:0 for i in range(1, n+2)}
        for item in nums:
            if item in d:
                d[item] = 1
        for value, key in zip(d.values(), d.keys()):
            if not value:
                return key

if __name__ == '__main__':
    s = Solution()
    nums = [0]
    print  s.firstMissingPositive(nums)
