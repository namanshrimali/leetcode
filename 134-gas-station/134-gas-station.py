class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
        if total_tank < 0:
            return -1
        curr_tank, start_pos = 0, 0
        for i in range(len(gas)):
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                start_pos = i + 1
                curr_tank = 0
        return start_pos