class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {')': '(', '}': '{', ']': '['}

        record = []

        for ch in s:
            if not record or ch not in parentheses_map:
                record.append(ch)
            else:
                key = parentheses_map[ch]
                if record[-1] == key:
                    record.pop()
                else:
                    record.append(ch)


        

        if record: 
            return False
        else:
             return True
        