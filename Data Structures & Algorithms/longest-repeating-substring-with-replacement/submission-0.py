class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapp = {}
        best_length = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            char = s[r]
            mapp[char] = 1 + mapp.get(char, 0)
            maxf = max(maxf, mapp[char])

            curr_length = r - l + 1
            diff = curr_length - maxf

            if diff > k:
                left_char = s[l]
                mapp[left_char] -= 1
                l += 1

            best_length = max(best_length, r - l + 1)
        
        return best_length
            
        