class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count_map, max_point = collections.defaultdict(int), 0
        known = {}
        for num in nums:
            count_map[num] += 1
            max_point = max(max_point, num)
        prev, second_prev = 0, 0
        for i in range(max_point+1):
            curr = max(prev, second_prev + i * count_map[i])
            second_prev = prev
            prev = curr
        return curr
                        