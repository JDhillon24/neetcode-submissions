class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxx = 0

        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
            maxx = max(maxx, curr_area)
        
        return maxx