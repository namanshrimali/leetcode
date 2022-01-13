class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(num_list = [], total = 0):
            nonlocal sol
            if total == target:
                sol.append(num_list[::])
                return
            for candidate in candidates:
                if num_list and candidate < num_list[-1]:
                    continue
                if total + candidate <= target:
                    backtracking(num_list+[candidate], total+candidate)
            
        sol = []
        backtracking()
        return sol
            
            