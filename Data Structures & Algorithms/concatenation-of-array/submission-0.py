class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        newcap = 2 * n
        ans = [0] * newcap


        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
         
        return ans