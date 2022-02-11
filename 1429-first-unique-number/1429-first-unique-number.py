class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = collections.deque(nums)
        self.counter = collections.defaultdict(int)
        for num in self.queue:
            self.counter[num]+=1

    def showFirstUnique(self) -> int:
        while self.queue:
            top_ele = self.queue[0]
            if self.counter[top_ele] == 1:
                return top_ele
            self.queue.popleft()
        return -1

    def add(self, value: int) -> None:
        self.queue.append(value)
        self.counter[value]+=1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)