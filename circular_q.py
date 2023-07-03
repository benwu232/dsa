class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.q = [0 for i in range(self.size)]
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            # print('Already full')
            return False
        elif self.rear == -1:
            self.front = 0
            self.rear = 0
            self.q[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.q[self.rear] = value
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            # print('Already Empty')
            return False
        elif self.front == self.rear:
            # out = self.q[self.front]
            self.front = self.rear = -1
        else:
            # out = self.q[self.front]
            self.front = (self.front + 1) % self.size
        return True
        

    def Front(self) -> int:
        if self.front == -1:
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.rear == -1:
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        if self.rear == -1 and self.front == -1:
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
mq.deQueue()
mq.enQueue(1)
print(mq.front, mq.rear)
mq.enQueue(2)
print(mq.front, mq.rear)
mq.enQueue(3)
print(mq.front, mq.rear)
print(mq.isFull())