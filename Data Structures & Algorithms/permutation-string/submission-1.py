
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        

        s1_map, s2_map = [0] * 26, [0] * 26

        # build maps for length of s1
        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] += 1
        

        # matches determine if # of char occurences map for each char
        matches = 0
        for i in range(26):
            matches += (1 if s1_map[i] == s2_map[i] else 0)

        
        left = 0

        for r in range(len(s1), len(s2)):
            # if all chars match then there's a permutation
            if matches == 26:
                return True

            # incrementing count of right pointer char
            index = ord(s2[r]) - ord('a')
            s2_map[index] += 1

            # if occurences for char is equal 
            if s1_map[index] == s2_map[index]:
                matches += 1
            # if increment undoes match
            elif s1_map[index] + 1 == s2_map[index]:
                matches -= 1
            
            # decrementing count of left ponter char
            index = ord(s2[left]) - ord('a')
            s2_map[index] -= 1

            # if occurences for char is equal
            if s1_map[index] == s2_map[index]:
                matches += 1
            # if decrement undoes match
            elif s1_map[index] - 1 == s2_map[index]:
                matches -= 1
            
            # move up left pointer
            left += 1


        return matches == 26

        