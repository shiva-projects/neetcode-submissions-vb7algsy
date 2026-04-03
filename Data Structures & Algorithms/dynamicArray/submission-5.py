class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.capacity = capacity
        self.insertelement = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.insertelement == self.capacity:
            self.resize()
        self.arr[self.insertelement] = n
        self.insertelement += 1


    def popback(self) -> int:
        self.insertelement -= 1
        return self.arr[self.insertelement]
    def resize(self):
        self.arr += [0] * self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.insertelement
    
    def getCapacity(self) -> int:
        return self.capacity