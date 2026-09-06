class MinStack:

    def __init__(self):
        self.record = []
        self.minvalues = []
        

    def push(self, val: int) -> None:
        self.record.append(val)

        if len(self.minvalues) == 0:
            self.minvalues.append(val)
        else:
            if val <= self.minvalues[-1]:
                self.minvalues.append(val)
        

    def pop(self) -> None:
        popped = self.record.pop()

        if len(self.minvalues) > 0:
            if self.minvalues[-1] == popped:
                self.minvalues.pop()
        

    def top(self) -> int:
        return self.record[-1]
        

    def getMin(self) -> int:
        return self.minvalues[-1]
        
