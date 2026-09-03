class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        maxnum = -1

        for i in range(len(arr) -1, -1, -1):
            val = arr[i]
            arr[i] = maxnum

            maxnum = max(val, maxnum)

        return arr
        
        


        
