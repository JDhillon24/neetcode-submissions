class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        

        def coinHelper(amount, cache):
            if amount < 0:
                return float("inf")
            elif amount == 0:
                return 0
            elif amount in cache:
                return cache[amount]
            
            res = float("inf")

            for coin in coins:
                res = min(res, 1 + coinHelper(amount - coin, cache))

            cache[amount] = res
            return res
        

        min_coins = coinHelper(amount, {})

        return min_coins if min_coins < float('inf') else -1
        