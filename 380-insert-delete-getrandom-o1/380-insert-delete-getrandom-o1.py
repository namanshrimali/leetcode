class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        val_idx = self.dict[val]
        self.arr[-1], self.arr[val_idx] = self.arr[val_idx], self.arr[-1]
        self.dict[self.arr[val_idx]] = val_idx
        del self.dict[self.arr.pop()]
        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()