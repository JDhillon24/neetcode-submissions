class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        l = 0
        res = [-1, -1]
        resLen = 10**6

        countS = {}
        countT = {}

       

        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
        
        have = 0
        need = len(countT)

        for r in range(len(s)):
            r_ch = s[r]

            countS[r_ch] = 1 + countS.get(r_ch, 0)
            
            if r_ch in countT and countS[r_ch] == countT[r_ch]:
                have += 1
            
            while have == need:
               
                if r - l + 1 < resLen:
                    res = [l,r]
                    resLen = r - l + 1
                    
                
                l_ch = s[l]
                countS[l_ch] -= 1
                l += 1

                if l_ch in countT and countS[l_ch] + 1 == countT[l_ch]:
                    have -= 1
                
        
        

        l, r = res
        return s[l:r + 1]