#coding:utf-8
class Solution(object):
    """
        题意：
            找到nums中绝对值之差为k的数字对，交换顺序的数字对无效。
            返回这样的数字对的个数

        题解：
            Time Complexity:O(N)
            Space Complexity:O(N)
            1.集合的 & 操作
            2.Counter操作(Counter对象其实就是一个字典，他这个类实现了帮你把数组变成计数字典的功能)
    """
    def findPairs(self, nums, k):
        if k > 0:
            return len(set(nums) & set(n+k for n in nums))
        elif k ==0:
            return sum(n>1 for n in Counter(nums).values())
        else:
            return 0



