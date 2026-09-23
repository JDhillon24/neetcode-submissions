class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for str in strs:
            char_map = {}

            for ch in str:
                char_map[ch] = 1 + char_map.get(ch, 0)

            key = tuple(sorted(char_map.items()))
            if key in groups:
                groups[key].append(str)
            else:
                groups[key] = [str]

        return list(groups.values())

        