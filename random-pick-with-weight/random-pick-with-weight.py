class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        self.total_sum = 0
        for weight in w:
            self.total_sum+=weight
            self.prefix_sums.append(self.total_sum)

    def pickIndex(self) -> int:
        random_no = random.random()*self.total_sum
        
        # for idx, prefix_sum in enumerate(self.prefix_sums):
        #     if random_no < prefix_sum:
        #         break
        low, high = 0, len(self.prefix_sums)-1
        while(low<high):
            mid = (low+high)//2
            if self.prefix_sums[mid] < random_no:
                low = mid+1
            else:
                high = mid
        # return idx
        return low