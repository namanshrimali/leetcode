class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_pass = [1,7,30]
        cost_dp = [None]*(max(days)+1)
        cost_dp[0] = 0
        j=0
        for i in range(1, len(cost_dp)):
            if i == days[j]:
                cost_dp[i] = min(cost_dp[max(0, i-day_pass[0])]+costs[0],cost_dp[max(0, i-day_pass[1])]+costs[1],cost_dp[max(0, i-day_pass[2])]+costs[2])  
                j+=1
            else:
                cost_dp[i] = cost_dp[i-1]
        return cost_dp[-1]