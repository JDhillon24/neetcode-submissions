class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        count = 0
        maxLen = 0
        prev = None

        if len(arr) < 2:
            return 1

        for i in range(len(arr) - 1):
            cur = arr[i]
            nextt = arr[i + 1]

            if cur == nextt:
                count = 1
                prev = None
            elif cur < nextt:
                count = count + 1 if prev == "up" else 2
                prev = "down"
            else:
                count = count + 1 if prev == "down" else 2
                prev = "up"
            
            maxLen = max(maxLen, count)
                

            
        
        return maxLen








        