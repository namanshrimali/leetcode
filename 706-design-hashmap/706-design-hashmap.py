class Bucket():
    def __init__(self):
        self.bucket = []
        
    def add(self, key, value):
        if not self._update(key, value):
            self.bucket.append([key, value])
        
    def _update(self, key, value):
        for i in range(len(self.bucket)):
            if self.bucket[i][0] == key:
                self.bucket[i][1] = value
                return True
        return False
                
    def search(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1
    
    def delete(self, key):
        for i in range(len(self.bucket)):
            if self.bucket[i][0] == key:
                self.bucket = self.bucket[:i]+self.bucket[i+1:]
                break

class MyHashMap:

    def __init__(self):
        self.map_size = 2069 # it's better to take prime numbers because it results in less collision.
        self.map = [Bucket() for i in range(self.map_size)]

    def put(self, key: int, value: int) -> None:
        bucket = self.map[key%self.map_size]
        bucket.add(key, value)
        

    def get(self, key: int) -> int:
        bucket = self.map[key%self.map_size]
        return bucket.search(key)
        

    def remove(self, key: int) -> None:
        bucket = self.map[key%self.map_size]
        bucket.delete(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)