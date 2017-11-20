#coding:utf-8
class Solution(object):
    def getRow(self, rowIndex):
        """
            思路：这道题和118题类似，主要可以利用杨辉三角的一个高级生成思路，就是每一级的数组可以由上一级的前后分别各添0 相加得到；
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x+y for x,y in zip([0] + row, row + [0])]
        return row

if __name__ == '__main__':
    s = Solution()
    print s.getRow(3)

