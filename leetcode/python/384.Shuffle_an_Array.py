#coding:utf-8
"""
这道题题意就是随机打乱一个数组
"""
class Solution(object):
	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.res = nums
	
	def reset(self):
		"""
		resets the array to its original configuration
		:rtype: List[int]
		"""
		return self.res
		
	def shuffle(self):
		"""
		shuffle the array
		"""
		ans = self.res[:]
		size = len(ans)
		for i in range(size):
			j = random.randint(0, size - 1)
			ans[i], ans[j] = ans[j], ans[i]
		return ans