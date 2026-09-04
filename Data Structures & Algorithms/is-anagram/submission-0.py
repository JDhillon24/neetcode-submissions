class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}

        for char in range(len(s)):
            char_s = s[char]
            char_t = t[char]

            if char_s not in s_map.keys():
                s_map[char_s] = 1
            else:
                s_map[char_s] += 1
            
            if char_t not in t_map.keys():
                t_map[char_t] = 1
            else:
                t_map[char_t] += 1
            
        return s_map == t_map

        