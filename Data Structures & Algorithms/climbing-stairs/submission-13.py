class Solution:
    def climbStairs(self, n: int) -> int:
        
        def helper(n, cache):
            if n <= 2:
                return n
            elif n in cache:
                return cache[n]
            
            cache[n] = helper(n-1, cache) + helper(n-2, cache)

            return cache[n]

        res = helper(n, {})

        return res
        