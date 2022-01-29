class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_visit_map = {}
        packed_tuple = sorted(zip(timestamp, username, website))
        for t, u, w in packed_tuple:
            website_list = user_visit_map.get(u, [])
            website_list.append(w)
            user_visit_map[u] = website_list
            
        pattern_count = {}
        for website_list in user_visit_map.values():
            combinations = set(itertools.combinations(website_list, 3))
            for combination in combinations:
                pattern_count[combination] = pattern_count.get(combination, 0)+1
        sorted_pattern = sorted(pattern_count, key=lambda x: (-pattern_count[x], x))
        return sorted_pattern[0]