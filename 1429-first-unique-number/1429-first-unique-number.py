class FirstUnique:

    def __init__(self, nums: List[int]):
        self.num_counter = {}
        self._count_numbers(nums)
        self.deque = collections.deque([])
        self._fill_nums(nums)
    

    def showFirstUnique(self) -> int:
        while self.deque and self.num_counter[self.deque[0]] > 1:
            self.deque.popleft()
        if not self.deque:
            return -1
        return self.deque[0]

    def add(self, value: int) -> None:
        self.num_counter[value] = self.num_counter.get(value, 0) + 1
        if self.num_counter[value] == 1:
            self.deque.append(value)
        
    def _count_numbers(self, nums):
        for num in nums:
            self.num_counter[num] = self.num_counter.get(num, 0) + 1
    def _fill_nums(self, nums):
        for num in nums:
            if self.num_counter[num] > 1:
                continue
            self.deque.append(num)
        
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)