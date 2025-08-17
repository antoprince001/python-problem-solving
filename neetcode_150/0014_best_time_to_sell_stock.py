# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProfitValue = 0
        # for i in range(0, len(prices)-1):
        #     for j in range(i, len(prices)):
        #         profitValue = prices[j] - prices[i]
        #         if profitValue > maxProfitValue:
        #             maxProfitValue = profitValue
        # return maxProfitValue
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = m y ax(max_profit, price - min_price)
        return max_profit
        
