class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        minimum = 1000
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
                if minimum > nums[mid]:
                    minimum = nums[mid]
            else:
                high = mid - 1
                if minimum > nums[mid]:
                    minimum = nums[mid]
            
        return minimum
