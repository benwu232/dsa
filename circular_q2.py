class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k + 1
        self.q = [0 for i in range(self.size)]
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            # print('Already full')
            return False
        else:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.size
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            # print('Already Empty')
            return False
        else:
            # out = self.q[self.front]
            self.front = (self.front + 1) % self.size
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.rear+self.size-1) % self.size]

    def isEmpty(self) -> bool:
        if self.rear == self.front:
            return True
        else:
            return False
        
    def isFull(self) -> bool:
        # print(self.rear, self.front, self.size)
        if (self.rear + 1) % self.size == self.front:
            return True
        else: 
            return False
        

mq = MyCircularQueue(3)
mq.enQueue(1)
mq.enQueue(2)
mq.enQueue(3)
print(mq.isFull())
mq.enQueue(1)


print(mq.deQueue())
print(mq.deQueue())
print(mq.deQueue())
print(mq.isEmpty())