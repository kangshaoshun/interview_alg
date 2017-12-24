#coding:utf-8
"""
    题意：反转字符串中的元音字母，比如hello ==> holle
    思路：将字符串中的元音字符，及位置添加进tmp_list，然后依次替换即可
"""
class Solution(object):
    def reverseVowels(self, s):
        vowel = 'AaEeIiOoUu'
        s_list = list(s)
        tmp_list = []
        for i, c in enumerate(s):
            if c in vowel:
                tmp_list.append((i, c))
        for i, c in enumerate(s_list):
            if c in vowel:
                s_list[i] = tmp_list[-1][1]
                tmp_list.pop()
        return ''.join(s_list)

if __name__ == '__main__':
    s = Solution()
    print s.reverseVowels('leetcode')
