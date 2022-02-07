class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        counter_map = collections.defaultdict(set)
        for first, second in roads:
            counter_map[second].add(first)
            counter_map[first].add(second)
        maximal_rank = 0
        for i in range(n):
            for j in range(i+1, n):
                maximal_rank = max(
                    maximal_rank, 
                    len(counter_map[i])+len(counter_map[j]) - (i in counter_map[j])
                )
        return maximal_rank