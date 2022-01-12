class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i+j in hash_map:
                    hash_map[i+j].insert(0, nums[i][j])
                else:  
                    hash_map[i+j] = [nums[i][j]]
        sol = []
        for key in hash_map:
            sol+=hash_map[key]
        return sol
        