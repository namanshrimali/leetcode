class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = collections.defaultdict(int)
        
        for num in nums:
            counter[num] += 1
        
        elements = sorted(counter.keys())
        prev_max, second_prev_max = elements[0] * counter[elements[0]], 0
        
        for i in range(1, len(elements)):
            num = elements[i]
            if num == elements[i-1] + 1:
                
                second_prev_max, prev_max = prev_max, max(prev_max, second_prev_max + counter[num]*num)
            else:
                second_prev_max, prev_max = prev_max, prev_max + counter[num]*num
        
        return prev_max
