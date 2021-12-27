class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        total = len(nums)
        neg_nos = []
        pos_nos = []
        
        for num in nums:
            if num < 0:
                neg_nos.insert(0, num**2)
            else:
                pos_nos.append(num**2)
        l, r = 0, 0
        sol = []
        while l<len(neg_nos) and r<len(pos_nos):
            if neg_nos[l]<pos_nos[r]:
                sol.append(neg_nos[l])
                l+=1
            else:
                sol.append(pos_nos[r])
                r+=1
        while l<len(neg_nos):
            sol.append(neg_nos[l])
            l+=1
        while r < len(pos_nos):
            sol.append(pos_nos[r])
            r+=1
        return sol
            
                