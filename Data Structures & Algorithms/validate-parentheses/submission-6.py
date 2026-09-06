class Solution:
    def isValid(self, s: str) -> bool:

        parentheses = {')': '(', '}': '{', ']': '['}
        record = []

        for p in s:
            if p not in parentheses.keys():
                record.append(p)
            else:
                if len(record) == 0:
                    return False
                elif parentheses.get(p) == record[-1]:
                    record.pop()
                else:
                    record.append(p)
                    
        
        if len(record) > 0:
            return False
        else:
            return True

        