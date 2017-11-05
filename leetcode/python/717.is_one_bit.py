#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class Solution(object):
    def isOneBitCharacter(self, bits):
        '''
            type bits:List[int]
            rtype:bool
        '''
        n = len(bits)
        i = 0
        while i < n:
            last = bits[i]
            if last == '1':
                i += 2
            else:
                i += 1
        return True if last == '0' else False




if __name__ == '__main__':
    '''
        思路：从头至尾遍历，如果是1，向后走两步，如果是0，向后走一步，直至走出界限，判断最后一个值是0还是1
    '''
    s = Solution()
    print s.isOneBitCharacter('100')
