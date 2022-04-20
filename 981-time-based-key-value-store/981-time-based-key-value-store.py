class Key:
    def __init__(self):
        self.values = []
        self.timestamps = []
        
    def get_value_for_timestamp(self, timestamp):
        left, right = 0, len(self.values)-1
        while left <= right:
            mid = (left+right)//2
            if self.timestamps[mid] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        if self.timestamps[right] > timestamp:
            return ''
        return self.values[right]
    
    def add_value_and_timestamp(self, value, timestamp):
        self.values.append(value)
        self.timestamps.append(timestamp)
    
class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = Key()
        self.keys[key].add_value_and_timestamp(value, timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.keys:
            return self.keys[key].get_value_for_timestamp(timestamp)
        return ''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)