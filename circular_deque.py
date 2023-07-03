class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.q = [None for i in range(self.size)]
        self.front = -1
        self.rear = -1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.front == -1 or self.rear == -1:
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front - 1) % self.size
        self.q[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.front == -1 or self.rear == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.size
        return True        
        
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]
        
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]   

    def isEmpty(self) -> bool:
        if self.front == -1 or self.rear == -1:
            return True
        return False
        

    def isFull(self) -> bool:
        if (self.front - 1) % self.size == self.rear \
            or (self.rear + 1) % self.size == self.front:
            return True
        return False

# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(8)
# param_1 = obj.insertFront(value)
print(obj.insertFront(5))
print(obj.getFront(1))
print(obj.insertLast(2))
print(obj.insertFront(3))
print(obj.insertFront(4))
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()