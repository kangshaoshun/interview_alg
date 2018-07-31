#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (24.86%)
# Total Accepted:    535.9K
# Total Submissions: 2.2M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# Examples:
# 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# 
# Given "bbbbb", the answer is "b", with the length of 1.
# 
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.
# 
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        解题思路：滑动窗口
        1.借助一个字典判断是否已经出现重复
        2.字典的value值保存的是元素出现的位置，如果出现重复，将窗口前沿 后移到重复元素上一个坐标的下一位。
        3.求得max(ans, ind + 1 - pre)即为最大不重复的长度

        T = O(N)
        S = O(N)
        """
        ans, pre = 0, 0
        d = dict()
        for ind, c in enumerate(s):
            if c not in d:
                d[c] = ind
            else:
                pre = max(d[c] + 1, pre)
                d[c] = ind
            ans = max(ans, ind + 1 - pre)
        return ans

if __name__ == "__main__":
    s = Solution()
    t = "abcabcbb"
    print s.lengthOfLongestSubstring(t)
