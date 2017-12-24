#coding:utf-8
"""
    判断学生根据出勤情况是否应该得到奖励
    思路：按照逻辑，不能出现A超过两次，不能出现LLL一次。问题就很简单了
"""
class Solution(object):
    def checkRecord(self, s):
        return s.count('A') < 2 and s.count('LLL') < 1


if __name__ == '__main__':
    s = Solution()
    print s.checkRecord('PPALLL')
        
