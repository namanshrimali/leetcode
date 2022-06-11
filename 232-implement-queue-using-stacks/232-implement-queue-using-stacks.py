class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        
    def _fill_out_stack(self):
        if len(self.out_stack) > 0:
            return
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        
    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._fill_out_stack()
        return self.out_stack.pop()
        

    def peek(self) -> int:
        self._fill_out_stack()
        return self.out_stack[-1]
        

    def empty(self) -> bool:
        self._fill_out_stack()
        return len(self.out_stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()