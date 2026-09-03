class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicate = False
        traversedNums = []

        for i in nums:
            if i in traversedNums:
                hasDuplicate = True
            
            traversedNums.append(i)
        

        return hasDuplicate