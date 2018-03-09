#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def nextGreatElement(self, findNums, nums):
        """
        :type findNums:List[int]
        :type nums: List[int]
        :rtype: List[int]
        思路：
            1.用findNum中的元素去nums中找 T = O(M * N) (舍弃)
            2.先将nums中的元素建立next great的栈，然后用findNum中的元素查找 O(N)
        """
        if not findNums:
            return []
        stack = []
        res_dict = {}
        for item in nums:
            if stack and stack[-1] < item:
                while stack and stack[-1] < item:
                    res_dict[stack.pop()] = item
                stack.append(item)
            else:
                stack.append(item)
        while stack:
            res_dict[stack.pop()] = -1
        res = []
        for item in findNum:
            res.append(res_dict[item])
        return res
