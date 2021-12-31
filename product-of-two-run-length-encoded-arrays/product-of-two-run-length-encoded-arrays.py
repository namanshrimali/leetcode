class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        sol = []
        i,j = 0, 0
        while(i<len(encoded1) and j<len(encoded2)):
            encoded1_message, encoded1_freq = encoded1[i]
            encoded2_message, encoded2_freq = encoded2[j]
            
            message = encoded1_message * encoded2_message
            freq = min(encoded1_freq, encoded2_freq)
            if sol and sol[-1][0] == message:
                sol[-1][1]+=freq
            else:
                sol.append([message, freq])
            encoded1[i][1]-=freq
            encoded2[j][1]-=freq
            
            if encoded1[i][1] == 0:
                i+=1
                
            if encoded2[j][1] == 0:
                j+=1
        return sol
        