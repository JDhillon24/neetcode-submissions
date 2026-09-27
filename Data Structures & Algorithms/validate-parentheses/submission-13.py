class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {')': '(', '}': '{', ']': '['}

        record = []

        for ch in s:
            if len(record) == 0 and ch in par_map:
                return False
            
            if ch not in par_map:
                record.append(ch)
            elif record[-1] == par_map.get(ch):
                record.pop()
            else:
                return False

        

        if len(record) > 0: 
            return False
        else:
             return True
        