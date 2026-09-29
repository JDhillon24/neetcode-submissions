class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        matches = 0

        l = 0
        s1_map = [0] * 26
        s2_map = [0] * 26

        k = len(s1)


        for ch in s1:
            s1_map[ord(ch) - ord('a')] += 1
        
        for i in range(26):
            if s1_map[i] == s2_map[i]:
                matches += 1

        for r in range(len(s2)):
            r_idx = ord(s2[r]) - ord('a')
            

            if s1_map[r_idx] == s2_map[r_idx]:
                matches -= 1
            s2_map[r_idx] += 1
            if s1_map[r_idx] == s2_map[r_idx]:
                matches += 1
            

            while r - l + 1 > k:
                l_idx = ord(s2[l]) - ord('a')
                

                if s1_map[l_idx] == s2_map[l_idx]:
                    matches -= 1
                s2_map[l_idx] -= 1
                if s1_map[l_idx] == s2_map[l_idx]:
                    matches += 1

                l += 1

            if matches == 26:
                return True

        return matches == 26