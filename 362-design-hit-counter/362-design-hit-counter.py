class HitCounter:

    def __init__(self):
        self.queue = [[0, 0]]*300

    def hit(self, timestamp: int) -> None:
        idx = timestamp%300
        time, count = self.queue[idx]
        if time == timestamp:
            self.queue[idx][1]+=1
        else:
            self.queue[idx] = [timestamp, 1]

    def getHits(self, timestamp: int) -> int:
        total = 0
        for time, count in self.queue:
            if timestamp-time < 300:
                total+=count
        return total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)