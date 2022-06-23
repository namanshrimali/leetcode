class KeyNode:
    def __init__(self):
        self.timestamps = []
        self.timestamp_values = []
    
    def get_value_for_timestamp(self, timestamp):
        left, right = 0, len(self.timestamps) - 1
        while left < right:
            mid = math.ceil((left+right)/2)
            if self.timestamps[mid] <= timestamp:
                left = mid
            else:
                right = mid - 1
        return '' if self.timestamps[left] > timestamp else self.timestamp_values[left]
    
    def set_timestamp_value(self, timestamp, value):
        self.timestamps.append(timestamp)
        self.timestamp_values.append(value)
        
class TimeMap:

    def __init__(self):
        self.key_timestamp_value_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_timestamp_value_map[key] = self.key_timestamp_value_map.get(key, KeyNode())
        key_node = self.key_timestamp_value_map[key]
        key_node.set_timestamp_value(timestamp, value)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_timestamp_value_map:
            return ""
        return self.key_timestamp_value_map[key].get_value_for_timestamp(timestamp)
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)