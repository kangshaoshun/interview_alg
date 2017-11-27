#coding:utf-8
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
            这是一道好题，面试中经常会遇到
            eg, [2, 6, 4, 8, 10, 9, 15]
            思路：将未排序的序列和排序之后的序列进行比对，不同前后第一个不同的地方即为需要排序的区间
            用到几个重要但容易忽视的知识点：
                sorted  :不改变源数组，返回结果（和sort区分）
                all     :所有元素为true才返回true
                [::-1]  :逆序输出序列

        """
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)

if __name__ == '__main__':
    s = Solution()
    nums = [2, 6, 4]
    print s.findUnsortedSubarray(nums)
