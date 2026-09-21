class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for char in s:
            s_map[char] = 1 + s_map.get(char, 0)
        
        for char in t:
            t_map[char] = 1 + t_map.get(char, 0)
        
        if s_map == t_map:
            return True
        else:
            return False
