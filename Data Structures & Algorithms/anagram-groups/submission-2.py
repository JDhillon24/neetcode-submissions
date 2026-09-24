class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # map that assigns empty list as default values for keys
        result = defaultdict(list)

        for str in strs:
            count = [0] * 26

            for ch in str:
                # increase count to appropriate spot in map
                count[ord(ch) - ord('a')] += 1

            # tuples are allowed as keys on map 
            result[tuple(count)].append(str)
        
        return list(result.values())
        