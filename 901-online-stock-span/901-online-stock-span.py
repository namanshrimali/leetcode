class StockSpanner:

    def __init__(self):
        self.stack = [(0, -1)]
        self.curr_idx = -1

    def next(self, price: int) -> int:
        self.curr_idx += 1
        while len(self.stack)>1 and self.stack[-1][0] <= price:
            self.stack.pop()
        self.stack.append((price, self.curr_idx))
        return self.stack[-1][1] - self.stack[-2][1]        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)