#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n:int
        :rtype: List[str]
        """

        """
            一个low逼的方法
            Time Complexity:O()
            Space Complexity:O()
        """
        def isGoodSolution(t):
            stack = []
            for item in t:
                if item == '(':
                    stack.append(item)
                if not stack:
                    return False
                if item == ')':
                    stack.pop()
            return stack == []

        s = ''
        for i in range(2 * n):
            if not s:
                res = [s+item for item in ['(', ')']]
                s = True
            else:
                res = [start + item for start in res for item in ['(', ')']]
        
        return [item for item in res if isGoodSolution(item)]

if __name__ == '__main__':
    s = Solution()
    print s.generateParenthesis(3)
