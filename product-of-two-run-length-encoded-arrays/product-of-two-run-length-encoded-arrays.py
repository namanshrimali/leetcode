class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i = 0
        sol = []
        while(encoded1 and encoded2):
            encoded1_message, encoded1_freq = encoded1[0]
            encoded2_message, encoded2_freq = encoded2[0]
            
            message = encoded1_message * encoded2_message
            freq = min(encoded1_freq, encoded2_freq)
            if sol and sol[-1][0] == message:
                sol[-1][1]+=freq
            else:
                sol.append([message, freq])
            
            if encoded1_freq-freq == 0:
                encoded1.pop(0)
            else:
                encoded1[0][1]-=freq
            if encoded2_freq-freq == 0:
                encoded2.pop(0)
            else:
                encoded2[0][1]-=freq
        return sol
        