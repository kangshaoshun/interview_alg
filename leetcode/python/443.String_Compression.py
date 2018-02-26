#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.
"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars:List[str]
        :rtype:int
        """
        pre = None
        res = ''
        for item in chars:
            if not pre:
                pre = item
                cnt = 1
            else:
                if pre == item:
                    cnt += 1
                else:
                    if cnt == 1:
                        res += pre
                    else:
                        res = res + pre + str(cnt)
                        cnt = 1
        if cnt == 1:
            res += pre
        else:
            res = res + pre + str(cnt)
        chars[:len(res)] = list(res)
        n = len(chars) - len(res)
        while n:
            chars.pop()
            n -= 1
        return len(chars)
