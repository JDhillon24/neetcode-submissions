class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for str in strs:
            count = [0] * 26

            for ch in str:
                idx = ord(ch) - ord('a')
                count[idx] += 1
            
            result[tuple(count)].append(str)
        
        return list(result.values())