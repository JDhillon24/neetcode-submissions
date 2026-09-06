class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {')': '(', '}': '{', ']': '['}

        record = []

        for char in s:
            if len(record) == 0 and char in par_map:
                return False
            
            if char not in par_map:
                record.append(char)
            elif record[-1] == par_map.get(char):
                record.pop()
            else:
                return False

        if len(record) > 0:
            return False
        else:
            return True