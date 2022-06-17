class RandomizedSet:

    def __init__(self):
        self.item_idx_map = {}
        self.item_array = []

    def insert(self, val: int) -> bool:
        if val in self.item_idx_map:
            return False
        self.item_idx_map[val] = len(self.item_array)
        self.item_array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.item_idx_map:
            return False
        val_idx = self.item_idx_map[val]
        self.item_array[val_idx], self.item_array[-1] = self.item_array[-1], self.item_array[val_idx]
        last_val = self.item_array[val_idx]
        self.item_idx_map[last_val] = val_idx
        self.item_array.pop()
        del self.item_idx_map[val]
        return True

    def getRandom(self) -> int:
        return self.item_array[random.randint(0, len(self.item_array)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()