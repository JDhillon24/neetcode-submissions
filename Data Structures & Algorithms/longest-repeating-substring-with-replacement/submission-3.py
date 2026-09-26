class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapp = {}
        maxfreq = 0
        maxx = 0
        l = 0

        for r in range(len(s)):
                 
            mapp[s[r]] = 1 + mapp.get(s[r], 0)
            maxfreq = max(maxfreq, mapp[s[r]])

            while (r - l + 1) - maxfreq > k:
                mapp[s[l]] -= 1
                l += 1

            maxx = max(maxx, r - l + 1)
        
        return maxx