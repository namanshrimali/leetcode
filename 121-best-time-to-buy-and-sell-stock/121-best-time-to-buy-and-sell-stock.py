class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = inf
        for price in prices:
            lowest = min(lowest, price)
            if price > lowest:
                max_profit = max(max_profit, price - lowest)
        return max_profit
        