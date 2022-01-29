class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        L = len(s)
        flips, ones = 0, 0
        # aim to always flip zeros
        for i in range(L):
            if s[i] == '1':
                ones+=1
            else:
                flips+=1    
            flips = min(ones, flips)
        return flips
    
    
    
    