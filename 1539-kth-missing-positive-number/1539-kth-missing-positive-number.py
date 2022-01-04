class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        counter = 0
        arr.insert(0, 0)
        for i in range(1, len(arr)):
            counter += arr[i]-arr[i-1]-1
            if counter >=k:
                return arr[i] - (counter - k) - 1
        return arr[i]+(k-counter)
            
                