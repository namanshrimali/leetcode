class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = list(str(n))
        L = len(n)
        i = L-2
        while(i>=0 and n[i]>=n[i+1]):
            i-=1
        if i == -1:
            return -1
        # index i will have first element that is less than number next to it
        min_idx = i+1   # finding min number that is greater than i
        for j in range(i+1, L):
            if n[j] > n[i] and n[j] <= n[min_idx]:
                min_idx = j
        n[min_idx], n[i] = n[i], n[min_idx]
        
        low, high = i+1, L-1
        while(low<high):
            n[low], n[high] = n[high], n[low]
            low+=1
            high-=1
        n =  int(''.join(n))
        return n if n < 1<<31 else -1

        
        