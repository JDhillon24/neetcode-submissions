class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = ''.join(filter(str.isalnum,s)).lower()

        k = len(cleaned_text) - 1

        for i in range(len(cleaned_text)):
            char_1 = cleaned_text[i]
            char_2 = cleaned_text[k]

            if char_1 != char_2:
                return False
            
            k -= 1
        
        return True
        