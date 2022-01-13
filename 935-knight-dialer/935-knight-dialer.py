class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        MAX = 10**9+7
        
        uniq_moment = []
        for i in range(n+1):
            uniq_moment.append([0]*10)
        
        def path(num, height=n):
            if uniq_moment[height][num] !=0:
                return uniq_moment[height][num]
            
            if height == 1:
                return 1
            
            total = 0
            
            for neighbor in neighbors[num]:
                total = (total + path(neighbor, height-1))%MAX
            uniq_moment[height][num] = total
            return total
        
        total = 0
        for i in range(10):
            total= (total+path(i, n))%MAX
        return total