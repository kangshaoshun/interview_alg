#coding:utf-8
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.78%)
# Total Accepted:    301.8K
# Total Submissions: 949.5K
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for ind, ch in enumerate(shortest):
            for other in strs:
                if other[ind] != ch:
                    return shortest[:ind]
        return shortest
        """
        空间复杂度比上面高一点
        if not strs or (len(strs) == 1 and strs[0] == ""):
            return ""
        res = []
        i = 0
        while True:
            try:
                tmp = set(map(lambda x:x[i], strs))
                if not tmp or len(tmp) != 1:
                    return ''.join(res)
                else:
                    res.append(tmp.pop())
                i += 1
            except:
                return ''.join(res)
        """

if __name__ == '__main__':
    s = Solution()
    strs = ["k"]
    print s.longestCommonPrefix(strs)
