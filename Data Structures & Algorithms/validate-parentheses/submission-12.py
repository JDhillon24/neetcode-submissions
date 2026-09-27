class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {')': '(', '}': '{', ']': '['}

        record = []

        for ch in s:
            if len(record) == 0 and ch in parentheses_map:
                return False
            
            if ch not in parentheses_map:
                record.append(ch)
            elif record[-1] == parentheses_map.get(ch):
                record.pop()
            else:
                return False

        

        if len(record) > 0: 
            return False
        else:
             return True
        