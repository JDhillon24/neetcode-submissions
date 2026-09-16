class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        curSum = 0

        for r in range(len(arr)):
            curSum += arr[r]

            if r >= k - 1:
                if curSum >= threshold * k:
                    count += 1
                curSum -= arr[r - k + 1]

        return count