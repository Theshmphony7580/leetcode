class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        
        min_buy = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < min_buy:
                min_buy = price
            max_profit = max(max_profit, price - min_buy)

                
        return max_profit

