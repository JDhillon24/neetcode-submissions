class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            a,b = s[l],s[r]

            if not a.isalnum():
                l += 1
            elif not b.isalnum():
                r -= 1
            elif a.lower() != b.lower():
                return False
            else:
                l += 1
                r -= 1

        
        return True
        