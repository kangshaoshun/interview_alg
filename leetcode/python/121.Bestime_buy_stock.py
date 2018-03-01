#coding:utf-8

class Solution(object):
    def maxProfit(self, prices):
        """
        if not prices:
            return 0
        for i in range(len(prices) -1):
            prices[i] = prices[i+1] - prices[i]
        max_profit = 0
        profit = 0
        for item in prices[:-1]:
            if profit + item > 0:
                profit += item
                if profit > max_profit:
                    max_profit = profit
            else:
                profit = 0
        return max_profit
        """
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
        return max_profit


if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([7,6,5,4])
