class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adjacency_list = {}
        for start, destination in tickets:
            if start not in adjacency_list:
                adjacency_list[start] = collections.deque()
            adjacency_list[start].append(destination)
        
        itenary = []
        
        def build_itenary(curr_loc):
            dest_list = [] if curr_loc not in adjacency_list else adjacency_list[curr_loc]
            while dest_list:
                    build_itenary(dest_list.popleft())
            itenary.append(curr_loc)
            
        build_itenary(curr_loc="JFK")
        return itenary[::-1]