class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = 10002
        max_profit = 0
        
        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            elif prices[i] - min_val > max_profit:
                max_profit = prices[i] - min_val
        return max_profit
