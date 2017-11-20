#coding:utf-8
"""
    原题链接：https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
    题意：求两个列表的交集，但是元素需保留原来的公共数量
    解题思路：
        利用Counter,也可以自己实现low逼一点的dict

    这里有一个新技术点：
        sum的新操作
        sum(para1, para2)
            提供两个参数，具体操作是，遍历第一个参数，对第一个参数的元素求和，然后 使用 + 操作符加到第二个参数上。要保证:
                para2的类型和para1求和完之后元素类型一致
                para1是iterable可迭代的
            eg.sum([1, 2], 3)  ===> 6
               sum(1, 2) == 错误，int不可迭代
               sum([[1,2]], []) ==> [1,2]
               sum([[1,2], [3,4]], []) ==> [1, 2, 3, 4]
               sum([[1, 2]], 4) ==错误 + 不能操作list 和 int 
                

"""
from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        return sum([[num] * min(c1[num], c2[num]) for num in c1&c2], [])


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print s.intersect(nums1, nums2)
