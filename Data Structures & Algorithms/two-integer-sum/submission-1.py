class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sum_map = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in sum_map:
                return [sum_map[diff], i]
            
            sum_map[n] = i
        