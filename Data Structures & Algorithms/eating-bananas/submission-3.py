class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        res = high = max(piles)
        


        while low <= high:
            mid = (low + high) // 2

            totalTime = 0

            for p in piles:
                totalTime += math.ceil(p / mid)
            
            if totalTime <= h:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        return res
        