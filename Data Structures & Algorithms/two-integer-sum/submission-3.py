class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}

        for idx, elem in enumerate(nums):
            val = target - elem
            if val in mapp:
                return [mapp[val], idx]
            mapp[elem] = idx
