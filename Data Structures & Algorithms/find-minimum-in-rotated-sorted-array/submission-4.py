class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        minimum = 1000
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            minimum = min(minimum, nums[mid])
            if nums[mid] > nums[high]:
                low = mid + 1
                minimum = min(minimum, nums[mid])
            else:
                high = mid - 1
 
            
        return min(minimum, nums[low])
