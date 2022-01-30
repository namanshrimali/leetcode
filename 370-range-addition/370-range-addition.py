class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        sol = [0]*length
        for start, end, inc in updates:
            sol[start]+=inc
            if end+1 < length:
                sol[end+1]-=inc
        for i in range(1, length):
            sol[i]+= sol[i-1]
        
        return sol
        