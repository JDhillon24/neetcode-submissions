class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dupes = set()
        max_length = 0

        for r in range(len(s)):
            while s[r] in dupes:
                dupes.remove(s[l])
                l += 1
        
            dupes.add(s[r])

            max_length = max(max_length, r - l + 1)

        
        return max_length