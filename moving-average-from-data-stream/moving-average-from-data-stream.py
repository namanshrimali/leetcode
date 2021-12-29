class MovingAverage:

    def __init__(self, size: int):
        self.queue = [0 for i in range(size)]
        self.size = size
        self.count = -1
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.count+=1
        tail = self.count%self.size
        self.window_sum+= val - self.queue[tail]
        self.queue[tail] =  val
        return self.window_sum/min(self.count+1, len(self.queue))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
