class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = {}

        res = 0 
        for r in range(len(s)):
            if s[r] in window:
                l = max(window[s[r]] + 1, l)
            
            window[s[r]] = r
            res = max(res, r - l + 1)
        
        return res
