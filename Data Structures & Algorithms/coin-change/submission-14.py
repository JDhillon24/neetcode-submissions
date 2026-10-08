class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        def helper(amount, cache):
            if amount == 0:
                return 0
            elif amount in cache:
                return cache[amount]

            
            res = 1e9

            for coin in coins:
                if coin <= amount:
                    res = min(res, 1 + helper(amount - coin, cache))
            
            cache[amount] = res
            return cache[amount]
        
        minCoins = helper(amount, {})

        return minCoins if minCoins < 1e9 else -1

