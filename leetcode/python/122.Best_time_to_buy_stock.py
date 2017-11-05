#coding:utf-8
'''
    Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit.

    设计思路：
        只要把每一个增长段get到就能获得最大利益
    Time Complexity:O(N)
    Space Complexity: O(1)
'''

class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        last = prices[0]
        profit = 0
        for item in prices:
            if item > last:
                profit += (item - last)
            last = item
        return profit




if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([1, 2, 3])
