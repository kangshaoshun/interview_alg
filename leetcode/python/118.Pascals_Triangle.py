#coding:utf-8
class Solution(object):
    def generate(self, numRows):
        """
            type numRows:int
            rtype:List[List[int]]
        """

        '''
        """
            Time Complexity:O(N^2)
            Space Complexity:O(N^2)
        """
        res = []
        for row in range(numRows):
            if not row:
                res.append([1])
            elif row == 1:
                res.append([1, 1])
            else:
                tmp_list = []
                for i in range(row + 1):
                    if i == 0 or i == row:
                        tmp_list.append(1)
                    else:
                        tmp_list.append(res[row-1][i-1] + res[row-1][i])
                res.append(tmp_list)
        return res
        '''
        #更优解
        res = []
        row = [1]
        for i in range(numRows):
            if not i:
                res.append(row)
            else:
                row = [x+y for x,y in zip([0] + row, row + [0])]
                res.append(row)
        return res
        
if __name__ == '__main__':
    s = Solution()
    print s.generate(5)

