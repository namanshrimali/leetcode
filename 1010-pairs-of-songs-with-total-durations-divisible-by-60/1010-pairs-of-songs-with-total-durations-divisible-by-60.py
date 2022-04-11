class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        total_pairs = 0
        found_map = {}
        for t in time:
            t_mod_60 = t%60
            if t_mod_60 == 0:
                total_pairs += found_map.get(0, 0)
            else:
                complement = 60-t_mod_60
                if complement in found_map:
                    total_pairs += found_map[complement]
            found_map[t_mod_60] = found_map.get(t_mod_60, 0) + 1
        return total_pairs