class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def can_send(age_x, age_y):
            if age_y > age_x or age_y <= 0.5*age_x+7:
                return 0
            elif age_y == age_x:
                return age_map[age_x]*(age_map[age_x]-1)
            return age_map[age_x]*age_map[age_y]
        
        age_map = {}
        for age in ages:
            age_map[age]= age_map.get(age, 0) + 1
        total_requests = 0
        for age_x in age_map:
            for age_y in age_map:
                total_requests+= can_send(age_x, age_y)
        return total_requests