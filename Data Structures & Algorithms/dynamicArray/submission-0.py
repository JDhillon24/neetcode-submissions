class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = []
        self.capacity = capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.getSize() == self.capacity:
            self.resize()
        
        self.arr.append(n)



    def popback(self) -> int:
        elem = self.arr.pop()
        return elem
 

    def resize(self) -> None:
        cap = self.capacity
        if len(self.arr) == cap:
            self.capacity = 2 * cap

    def getSize(self) -> int:
        return len(self.arr)
        
    
    def getCapacity(self) -> int:
        return self.capacity
