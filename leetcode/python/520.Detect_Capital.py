#coding:utf-8
"""
    识别一个word是否是一个Captial,三种情况是Captial:
        1.全是大写
        2.全是小写
        3.首字母大写，其他都是小写
"""
class Solution(object):
    def detectWordCaptial(self, word):
        return any((word.islower(), word.isupper(), word[0].isupper() and word[1:].islower()))


if __name__ == '__main__':
    s = Solution()
    print s.detectWordCaptial('kang')

