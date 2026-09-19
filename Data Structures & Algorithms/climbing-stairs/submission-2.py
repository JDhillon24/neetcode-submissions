class Solution:
    def climbStairs(self, n: int) -> int:
        mapp = {}

        def helper(k: int) -> int:
            if k <= 3:
                return k
            if k in mapp:
                return mapp[k]
            
            mapp[k] = helper(k-1) + helper(k-2)
            return mapp[k]
        
        return helper(n)