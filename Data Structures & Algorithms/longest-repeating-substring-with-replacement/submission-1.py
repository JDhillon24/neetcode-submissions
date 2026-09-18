class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # map to contain frequencies of characters
        mapp = {}
    
        # init left pointer, best substring length, # of most freq char
        l = 0
        best_length = 0
        maxf = 0

        for r in range(len(s)):
            # add char to map and compute max frequency
            mapp[s[r]] = 1 + mapp.get(s[r], 0)
            maxf = max(maxf, mapp[s[r]])


            # # of replacements = substring length - max freq
            diff = (r - l + 1) - maxf
            if diff > k:
                mapp[s[l]] -= 1
                l += 1
            
            best_length = max(best_length, r - l + 1)
        
        return best_length




        