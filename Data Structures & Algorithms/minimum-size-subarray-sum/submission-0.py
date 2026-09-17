class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # initialize left pointer, total sum, and subarray length variable
        l = 0
        total = 0
        length = float("inf")

        # increment through list
        for r in range(len(nums)):
            # update total
            total += nums[r]

            # check window size and shrink conditionally
            while total >= target:

                length = min(length, r - l + 1)

                total -= nums[l]
                l += 1
            
        # if length hasn't changed no subarrays met the conditions
        return 0 if length == float("inf") else length

