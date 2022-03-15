class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count_map, max_point = collections.defaultdict(int), 0
        known = {}
        for num in nums:
            count_map[num] += 1
            max_point = max(max_point, num)
        
        def max_points(num):
            if num in known:
                return known[num]
            if num == 0 or num == 1:
                return count_map.get(num, 0)
            known[num] = max(max_points(num-1), max_points(num-2)+ num * count_map[num])
            return known[num]
        
        return max_points(max_point)
                        