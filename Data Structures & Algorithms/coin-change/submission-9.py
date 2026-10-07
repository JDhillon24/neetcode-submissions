class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
       

        def helper(amount, cache):
            if amount == 0:
                return 0
            elif amount in cache:
                return cache[amount]
            
            res = 10000

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + helper(amount - coin, cache))
            
            cache[amount] = res
            return res
        
        minCoins = helper(amount, {})

        return -1 if minCoins >= 10000 else minCoins
