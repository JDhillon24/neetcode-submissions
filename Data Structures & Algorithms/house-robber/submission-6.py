class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        
        def helper(i, cache):
            if i >= len(nums):
                return 0
            elif i in cache:
                return cache[i]
            
            cache[i] = max(helper(i + 1, cache), nums[i] + helper(i + 2, cache))

            return cache[i]
        
        return helper(0, {})
