class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {')': '(', '}': '{', ']': '['}

        record = []

        for ch in s:
            if not record and ch in parentheses_map:
                return False
            
            if ch not in parentheses_map:
                record.append(ch)
            elif record[-1] == parentheses_map.get(ch):
                record.pop()
            else:
                return False

        

        if record: 
            return False
        else:
             return True
        