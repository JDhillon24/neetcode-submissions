class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxim = -1

        for i in range(len(arr) - 1, -1, -1):
            val = arr[i]
            arr[i] = maxim

            maxim = max(val, maxim)
        
        return arr
        