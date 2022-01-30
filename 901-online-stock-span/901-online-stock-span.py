class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if self.stack:
            count, i = 1, len(self.stack)-1
            while(i>=0 and self.stack[i][0]<=price):
                count+=self.stack[i][1]
                i-=self.stack[i][1]
            self.stack.append((price, count))
        else:
            self.stack.append((price, 1))
        
        return self.stack[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)