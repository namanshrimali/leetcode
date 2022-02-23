class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        adjacency_dict = collections.defaultdict(set)
        
        for p1, p2 in dislikes:
            adjacency_dict[p1].add(p2)
            adjacency_dict[p2].add(p1)
        
        self.colour = [0]*(n+1)
        
        def dfs(key, colour):
            self.colour[key] = colour
            
            for adjacent in adjacency_dict[key]:
                if self.colour[adjacent] == colour:
                    return False
                if self.colour[adjacent] == 0 and not(dfs(adjacent, -colour)):
                    return False
            return True
            
        for key in adjacency_dict:
            if self.colour[key] != 0:
                continue
            if dfs(key, 1) == False:
                return False
        return True