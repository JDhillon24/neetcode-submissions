class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        k = len(s1)
        l = 0
        

        s1_map = [0] * 26
        s2_map = [0] * 26

        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] += 1
        
        
        matches = 0

        for i in range(26):
            if s1_map[i] == s2_map[i]:
                matches += 1

        for r in range(k, len(s2)):
            if matches == 26:
                return True
            
            r_ch = ord(s2[r]) - ord('a')
            s2_map[r_ch] += 1

            if s2_map[r_ch] == s1_map[r_ch]:
                matches += 1
            elif s2_map[r_ch] - 1 == s1_map[r_ch]:
                matches -= 1
            
            while (r - l + 1) > k:
                l_ch = ord(s2[l]) - ord('a')
                s2_map[l_ch] -= 1

                if s2_map[l_ch] == s1_map[l_ch]:
                    matches += 1
                elif s2_map[l_ch] + 1 == s1_map[l_ch]:
                    matches -= 1
                
                l += 1
            
        return matches == 26

