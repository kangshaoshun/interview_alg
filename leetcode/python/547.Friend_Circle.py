#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M:List[List[int]]
        :rytpe :int
        """
        """
            M: m * n
            Time Complexity:O(m * n)
            Space Complexity:O(m)
        """
        cnt = 0
        N = len(M)
        seen = set()
        def dfs(node):
            for index, nei in enumerate(M[node]):
                if nei and index not in seen:
                    seen.add(index)
                    dfs(index)
        for i in range(N):
            if i not in seen:
                dfs(i)
                cnt += 1
        return cnt

if __name__ == '__main__':
    s = Solution()
    M = [[1,1,0],[1,1,1],[0,1,1]]
    print s.findCircleNum(M)
