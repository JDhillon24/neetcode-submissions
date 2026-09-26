class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""
        
        l = 0
        res = [-1,-1]
        resLen = 10 ** 6

        countS = {}
        countT = {}


        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
        
        need = len(countT)
        have = 0
        
        for r in range(len(s)):
            rch = s[r]
            countS[rch] = 1 + countS.get(rch, 0)

            if rch in countT and countS[rch] == countT[rch]:
                have += 1

            while have == need:

                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1

                lch = s[l]
                countS[lch] -= 1
                if lch in countT and countS[lch] < countT[lch]:
                    have -= 1
                
                

                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""
    
