class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        record = []

        for token in tokens:
            if token == "+":
                a = record.pop()
                b = record.pop()
                c = int(b) + int(a)
                record.append(c)
            elif token == "-":
                a = record.pop()
                b = record.pop()
                c = int(b) - int(a)
                record.append(c)
            elif token == "*":
                a = record.pop()
                b = record.pop()
                c = int(b) * int(a)
                record.append(c)
            elif token == "/":
                a = record.pop()
                b = record.pop()
                c = int(b) / int(a)
                record.append(c)
            else:
                record.append(token)
        
        return int(record[0])