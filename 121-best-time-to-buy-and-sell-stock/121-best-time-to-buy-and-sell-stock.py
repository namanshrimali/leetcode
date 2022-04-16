class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price, max_profit = prices[0], 0
        for price in prices[1:]:
            if price <= lowest_price:
                lowest_price = price
            else:
                profit = price-lowest_price
                max_profit = max(profit, max_profit)
        return max_profit
        