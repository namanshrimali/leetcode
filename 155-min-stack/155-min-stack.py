class MinStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        self.deleted = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.heap, val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        self.deleted[val] = self.deleted.get(val, 0) + 1

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        while self.heap and self.heap[0] in self.deleted:
            val = heapq.heappop(self.heap)
            self.deleted[val]-=1
            if self.deleted[val] == 0:
                del self.deleted[val]
            
        return self.heap[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()