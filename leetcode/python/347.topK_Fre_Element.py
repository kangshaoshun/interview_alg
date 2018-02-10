#coding:utf-8
import sys
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums:List[int]
        :type k:int
        :rtype: List[int]
        """
        """
        Time Complexity:O(nlogn)
        Space Complexity:O(n)
        """
        return [item[0] for item in sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True)[:k]]


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    s = Solution()
    print s.topKFrequent(nums, k)



