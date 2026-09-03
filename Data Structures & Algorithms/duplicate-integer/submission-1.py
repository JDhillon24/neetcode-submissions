class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        traversedNums = {}

        for i in nums:

            string = f"{i}"
            if string in traversedNums:
                return True

            traversedNums[string] = i
        

        return False