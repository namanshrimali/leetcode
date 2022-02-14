class Solution:

    def __init__(self, w: List[int]):
        self.prefix_weights = [w[0]]
        for i in range(1, len(w)):
            self.prefix_weights.append(self.prefix_weights[i-1] + w[i])

    def pickIndex(self) -> int:
        rand_num = random.random() * self.prefix_weights[-1]
        left, right = 0, len(self.prefix_weights)
        while left<right:
            mid = (left+right)//2
            if self.prefix_weights[mid] < rand_num:
                left = mid+1
            else:
                right = mid
        return right
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()