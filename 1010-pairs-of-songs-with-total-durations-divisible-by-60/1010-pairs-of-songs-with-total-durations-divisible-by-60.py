class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder_counter = {}
        total_pairs = 0
        for t in time:
            remainder = t % 60
            complement = 60 - remainder
            
            if remainder == 0 and 0 in remainder_counter:
                total_pairs += remainder_counter[remainder]
            elif complement in remainder_counter:
                total_pairs += remainder_counter[complement]
            
            
            remainder_counter[remainder] = remainder_counter.get(remainder, 0) + 1
        return total_pairs