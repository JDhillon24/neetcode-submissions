class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverseString(s: List[str], high: int, low: int) -> None:
            if low >= high:
                return
            
            s[low], s[high] = s[high], s[low]
            reverseString(s, high - 1, low + 1)
        
        reverseString(s, len(s) - 1, 0)