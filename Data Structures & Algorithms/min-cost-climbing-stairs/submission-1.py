class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        def helper(i, cache):
            if i > len(cost) - 1:
                return 0
            elif i in cache:
                return cache[i]

            res = float("inf")

            res = cost[i] + min(helper(i+1, cache), helper(i+2, cache))
            cache[i] = res

            return cache[i]
            
        
        return min(helper(0, {}), helper(1, {}))