class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        record = []

        for op in tokens:
            if op == '+':
                a, b = record.pop(), record.pop()
                num = int(b + a)
                record.append(num)
            elif op == '-':
                a, b = record.pop(), record.pop()
                num = int(b - a)
                record.append(num)
            elif op == '*':
                a, b = record.pop(), record.pop()
                num = int(b * a)
                record.append(num)
            elif op == '/':
                a, b = record.pop(), record.pop()
                num = int(b / a)
                record.append(num)
            else:
                record.append(int(op))
        
        return record.pop()
