class Solution:
    def calPoints(self, operations: List[str]) -> int:

        record = []

        for i in range(len(operations)):
            if operations[i] == '+':
                old_1 = record.pop()
                old_2 = record.pop()
                new_score = old_1 + old_2

                record.append(old_2)
                record.append(old_1)
                record.append(new_score)

            elif operations[i] == 'D':
                record.append(2 * int(record[-1]))
            elif operations[i] == 'C':
                record.pop()
            else:
                record.append(int(operations[i]))
        
        return sum(record)
        