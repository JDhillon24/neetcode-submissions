class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        res = []

        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)
        
        freq = [[] for i in range(len(nums) + 1)]

        for num,count in count_map.items():
            freq[count].append(num)
        
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res
        