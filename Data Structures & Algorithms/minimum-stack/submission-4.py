class MinStack:

    def __init__(self):
        self.record = []
        self.minval = []
        

    def push(self, val: int) -> None:
        self.record.append(val)

        if not self.minval:
            self.minval.append(val)
        elif self.getMin() >= val:
            self.minval.append(val)
        

    def pop(self) -> None:
        popped = self.record.pop()

        if self.getMin() == popped:
            self.minval.pop()

    def top(self) -> int:
        return self.record[-1]
        

    def getMin(self) -> int:
        return self.minval[-1]
        
