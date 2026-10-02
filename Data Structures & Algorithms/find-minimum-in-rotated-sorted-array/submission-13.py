class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        minimum = 1000

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
                minimum = min(minimum, nums[mid])
            else:
                high = mid - 1
                minimum = min(minimum, nums[mid])


        return minimum   
        