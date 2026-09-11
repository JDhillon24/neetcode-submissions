class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        record = []

        
        for op in tokens:
            if op == '+':
                a, b = record.pop(), record.pop()
                record.append(b + a)
            elif op == '-':
                a, b = record.pop(), record.pop()
                record.append(b - a)
            elif op == '*':
                a, b = record.pop(), record.pop()
                record.append(b * a)
            elif op == '/':
                a, b = record.pop(), record.pop()
                record.append(int(b / a))
            else:
                record.append(int(op))
        return record.pop()
        