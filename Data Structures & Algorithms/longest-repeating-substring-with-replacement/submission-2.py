class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapp = {}
        maxfreq = 0
        maxx = 0
        l = 0

        for r in range(len(s)):
            window_length = r - l + 1

                  
            count = 1 + mapp.get(s[r], 0)

            mapp[s[r]] = count
            maxfreq = max(maxfreq, count)

            if window_length - maxfreq > k:
                mapp[s[l]] -= 1
                l += 1

            maxx = max(maxx, r - l + 1)
        
        return maxx