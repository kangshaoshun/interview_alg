#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        DP
        dp[n] = min(dp[n-1], dp[n-2]) + cost[n]
        Time Complexity:O(N)
        Space Complexity:O(N)
        """
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
        return min(dp[-1], dp[-2])

if __name__ == '__main__':
    s = Solution()
    print s.minCostClimbingStairs([10, 15, 20])
