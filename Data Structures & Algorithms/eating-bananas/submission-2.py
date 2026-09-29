class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)   
        res = high
        while low <= high:
            totalTime = 0
            mid = (low + high) // 2

            for p in piles:
                totalTime += math.ceil(p / mid)
            
            if totalTime <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res


