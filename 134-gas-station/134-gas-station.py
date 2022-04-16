class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        total_tank = 0
        
        for i in range(n):
            total_tank += gas[i] - cost[i]
        
        if total_tank < 0:  # no solution exists
            return -1
            
        # solution exists
        curr_tank, start_pos = 0, 0
        
        for i in range(n):
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                start_pos = i + 1
                curr_tank = 0
        
        return start_pos