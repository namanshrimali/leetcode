class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        total = sum(ribbons)
        if k > total:
            return 0
        start, end = 1, min(total//k, max(ribbons))
        while start<end:
            mid = (start+end+1)//2
            sum_ = sum(ribbon//mid for ribbon in ribbons)
            if sum_ >= k:
                start = mid
            else:
                end=mid-1
        return start
            
                