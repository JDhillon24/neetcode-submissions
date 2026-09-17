class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        max_ones = 0
        replaced = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                replaced += 1
            
            while replaced > 1:
                if nums[l] == 0:
                    replaced -= 1
                l += 1
            
            max_ones = max(max_ones, r - l + 1)
        
        return max_ones
            
        