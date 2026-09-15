class MinStack:

    def __init__(self):
        self.record = []
        self.minvals = []

    def push(self, val: int) -> None:
        if not self.minvals:
            self.minvals.append(val)
        elif self.minvals[-1] >= val:
            self.minvals.append(val)

        self.record.append(val)        
        

    def pop(self) -> None:

        popped_val = self.record.pop()
        
        if popped_val == self.minvals[-1]:
            self.minvals.pop() 
        

    def top(self) -> int:
        return self.record[-1]

    def getMin(self) -> int:
        return self.minvals[-1]
        
