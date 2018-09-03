#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
翻转单词顺序

左旋转字符串顺序
"""

class Solution(object):
    def rotate_words_all(self, string):
        if not string:return ''
        s_list = string.split(' ')
        return ' '.join(reversed(s_list))

    def rotate_words_part(self, s, k):
        if not s:return ""
        s_list = list(s)
        assert k > -1, 'k must be larger 0'
        k = k % len(s)
        if k == 0:return s
        i, j = 0, k - 1
        while i < j:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1
        i, j = k, len(s) - 1
        while i < j:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1
        return ''.join(reversed(s_list))

if __name__ == '__main__':
    s = Solution()
    #print s.rotate_words_all("I am a student.")
    print s.rotate_words_part('abcdefg', int(sys.argv[1]))
