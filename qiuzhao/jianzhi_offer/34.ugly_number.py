#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
丑数

只能被2 、3、5 整除的数

习惯上称1位第一个丑数
"""
class Solution(object):
    def get_ugly_number(self, k):
        if k < 0:
            return -1
        ugly_list = [1]
        two, three, five = 0, 0, 0
        cnt = 1
        while cnt < k:
            ugly_tmp = min(2 * ugly_list[two], 3 * ugly_list[three], 5 * ugly_list[five])
            ugly_list.append(ugly_tmp)
            while 2 * ugly_list[two] <= ugly_tmp:
                two += 1
            while 3 * ugly_list[three] <= ugly_tmp:
                three += 1
            while 5 * ugly_list[five] <= ugly_tmp:
                five += 1
            cnt += 1
        return ugly_list[-1]


if __name__ == '__main__':
    s = Solution()
    print s.get_ugly_number(int(sys.argv[1]))

