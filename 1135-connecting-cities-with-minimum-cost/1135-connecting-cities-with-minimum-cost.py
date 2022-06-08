class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        self.weights = [1]*(n+1)
    
    def union(self, city_1, city_2):
        city_1_parent, city_2_parent = self.find_parent(city_1), self.find_parent(city_2)
        
        if self.weights[city_1_parent] > self.weights[city_2_parent]:
            self.parents[city_2_parent] = city_1_parent
            self.weights[city_1_parent] += self.weights[city_2_parent]
        else:
            self.parents[city_1_parent] = city_2_parent
            self.weights[city_2_parent] += self.weights[city_1_parent]
    
    def are_connected(self, city_1, city_2):
        parent_city_1, parent_city_2 = self.find_parent(city_1), self.find_parent(city_2)
        return parent_city_1 == parent_city_2
        
    def find_parent(self, city):
        while self.parents[city] != city:
            self.parents[city] = self.parents[self.parents[city]]
            city = self.parents[city]
        return city
    
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key = lambda connection: connection[2])
        disjoint_set = DisjointSet(n)
        total_cost, total_connections = 0, 0
        for city_1, city_2, cost in connections:
            if disjoint_set.are_connected(city_1, city_2):
                continue
            disjoint_set.union(city_1, city_2)
            total_cost += cost
            total_connections += 1
        
        return total_cost if total_connections == n-1 else -1
        