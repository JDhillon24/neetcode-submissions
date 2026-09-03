class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cnt = 0

        for i in nums:
            if i == 1:
                cnt += 1
            else:
                res = max(res,cnt)
                cnt = 0
            res = max(res,cnt)
        
        return res

        