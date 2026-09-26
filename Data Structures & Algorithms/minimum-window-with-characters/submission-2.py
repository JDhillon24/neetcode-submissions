class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if s == t:
            return s
        elif len(t) > len(s):
            return ""
        
        l = 0
        minimum = None

        countS = {}
        countT = {}


        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
        
        need = len(countT)
        have = 0
        
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)

            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1

            while have == need:

                if not minimum or len(minimum) > r - l + 1:
                    minimum = s[l : r + 1]

                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                
                

                l += 1

        if not minimum:
            return ""
        else: 
            return minimum
    
