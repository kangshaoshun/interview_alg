#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
字符串的全排列

可以推广到数组的全排列等等

"""
class Solution(object):
    def __init__(self):
        self.result = []

    def helper(self, fro, to, sl):
        if fro == to - 1:
            self.result.append(''.join(sl))
        else:
            for j in range(fro, to):
                #tmp = nums[:]  如果是数组的全排列
                sl[fro], sl[j] = sl[j], sl[fro]
                self.helper(fro + 1, to, sl)
                sl[fro], sl[j] = sl[j], sl[fro]

    def permutation(self, s):
        length = len(s)
        if length <= 1:return s
        sl = list(s)
        self.helper(0, length, sl)
        return self.result


if __name__ == '__main__':
    so = Solution()
    print so.permutation('abcd')
