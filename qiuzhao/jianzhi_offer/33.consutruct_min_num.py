#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
构成最小数
"""
class Solution(object):
    def construct_min_num(self, nums):
        def comp(x, y):
            tmp1 = str(x) + str(y)
            tmp2 = str(y) + str(x)
            if tmp1 > tmp2:
                return 1
            elif tmp2 > tmp1:
                return -1
            else:
                return 0

        nums.sort(cmp=comp)
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = s.construct_min_num(eval(sys.argv[1]))
    print ''.join(map(str, nums))

