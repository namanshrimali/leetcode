class MaxStack:

    def __init__(self):
        self.max_heap = []
        self.recency_stack = []
        self.soft_deleted = set()
        self.next_id = 0
        
    def push(self, x: int) -> None:
        heapq.heappush(self.max_heap, (-x, self.next_id))
        self.recency_stack.append((x, self.next_id))
        self.next_id-=1

    def pop(self) -> int:
        value, timestamp = self.recency_stack.pop()
        self.soft_deleted.add(timestamp)
        self._cleanup()
        return value
        
    def _cleanup(self):
        while self.max_heap and self.max_heap[0][1] in self.soft_deleted:
            self.soft_deleted.remove(heapq.heappop(self.max_heap)[1])
        while self.recency_stack and self.recency_stack[-1][1] in self.soft_deleted:
            self.soft_deleted.remove(self.recency_stack.pop()[1])
            
    def top(self) -> int:
        return self.recency_stack[-1][0]
        
    def peekMax(self) -> int:
        return -self.max_heap[0][0]

    def popMax(self) -> int:
        value, timestamp = heapq.heappop(self.max_heap)
        self.soft_deleted.add(timestamp)
        self._cleanup()
        return -value


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()