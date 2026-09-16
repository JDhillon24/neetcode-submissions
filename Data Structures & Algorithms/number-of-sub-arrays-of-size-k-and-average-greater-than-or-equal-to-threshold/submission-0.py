class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        l = 0
        r = l + k

        while r <= len(arr):
            avg = sum(arr[l:r]) / k

            if avg >= threshold:
                count += 1
            
            l += 1
            r += 1

        return count