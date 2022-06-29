class DisjointSet:
    def __init__(self, total_points):
        self.parents = [i for i in range(total_points)]
        self.weights = [1] * total_points
        self.total_points = total_points

    def union(self, city_a, city_b):
        parent_a, parent_b = self.find_parent(city_a), self.find_parent(city_b)
        if parent_a == parent_b:
            return
        if self.weights[parent_a] > self.weights[parent_b]:
            self.parents[parent_b] = parent_a
            self.weights[parent_a] += self.weights[parent_b]
        else:
            self.parents[parent_a] = parent_b
            self.weights[parent_b] += self.weights[parent_a]
    
    def find_parent(self, city):
        while self.parents[city] != city:
            self.parents[city] = self.parents[self.parents[city]]
            city = self.parents[city]
        return city
    
    def are_connected(self, city_a, city_b):
        return self.find_parent(city_a) == self.find_parent(city_b)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        province_set = DisjointSet(n)
        
        for city_a in range(n):
            for city_b in range(city_a + 1, n):
                if isConnected[city_a][city_b] == 1:
                    province_set.union(city_a, city_b)
    
        unique_provinces = set()
        for i in range(n):
            unique_provinces.add(province_set.find_parent(i))
        
        return len(unique_provinces)