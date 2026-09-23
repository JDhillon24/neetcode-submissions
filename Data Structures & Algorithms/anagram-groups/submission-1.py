class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for str in strs:
            count = [0] * 26

            for ch in str:
                count[ord(ch) - ord('a')] += 1
            
            result[tuple(count)].append(str)

        return list(result.values())

        