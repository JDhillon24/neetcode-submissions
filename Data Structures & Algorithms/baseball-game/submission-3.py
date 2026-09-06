class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == '+':
                top_1 = record.pop()
                top_2 = record.pop()

                newval = top_1 + top_2

                record.append(top_2)
                record.append(top_1)
                record.append(newval)
            elif op == 'D':
                newval = 2 * record[-1]
                record.append(newval)
            elif op == 'C':
                record.pop()
            else:
                record.append(int(op))
        
        return sum(record)
        