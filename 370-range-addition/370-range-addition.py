class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        output = [0]*length
        for start_idx, end_idx, inc in updates:
            output[start_idx]+= inc
            if end_idx+1 < length:
                output[end_idx+1] += -inc
        for i in range(1, length):
            output[i] += output[i-1]
        return output
    
        
        
        