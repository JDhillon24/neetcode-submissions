class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {1 : 1, 2 : 2, 3 : 3}

        def memoization(n, cache):
            if n <= 3:
                return n
            elif n in cache:
                return cache[n]
            
            cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)

            return cache[n]


        return memoization(n, cache)
