class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set profit and left pointer to 0
        l = 0
        profit = 0

        # traverse through prices
        for r in range(len(prices)):
            # if selling price is lower than buy, it becomes new buy
            if prices[r] < prices[l]:
                l = r
            
            # profit either stays 0 or current best profit
            profit = max(profit, prices[r] - prices[l])
        
        return profit

        
        