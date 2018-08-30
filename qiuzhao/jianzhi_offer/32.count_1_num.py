#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def count_one_num(self, n):
        if n < 0:
            return 0
        cnt = 0
        for i in range(1, n + 1):
            while i:
                cnt += ((i % 10) == 1)
                i /= 10
        return cnt


if __name__ == '__main__':
    s = Solution()
    print s.count_one_num(int(sys.argv[1]))

