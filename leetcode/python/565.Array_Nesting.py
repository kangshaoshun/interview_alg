#coding:utf-8
"""
    题意：数组长度n,找出长度最大的数组圈
    {A[i], A[A[i]], A[A[A[i]]] ...}
"""

"""
    解题思路：
        数组中的圆圈，有这样的规律，如果A[i] 被访问了，则属于它这个圆上的节点都将会被访问，而不属于它这个圆的节点将不会被访问，当遍历到一个节点没有被访问的时候，那么属于没有被访问的节点的圆也只可能从没有被访问的节点中得来。
"""
class Solution(object):
    def arrayNesting(self, nums):
        """
            type nums:List[int]
            rtype: int
        """
        ans, step, n = 0, 0, len(nums)
        seen = [False] * n
        for i in range(n):
            while not seen[i]:
                seen[i] = True
                i, step = nums[i], step + 1
            ans = max(ans, step)
            step = 0
        return ans
