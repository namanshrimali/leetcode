class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbours = set()
    def add_neighbour(self, neighbour):
        self.neighbours.add(neighbour)
    def remove_neighbour(self, neighbour):
        self.neighbours.remove(neighbour)
    def is_leaf(self):
        return len(self.neighbours) == 1
        
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        nodes_map = {}
        
        for node1, node2 in edges:
            if node1 not in nodes_map:
                nodes_map[node1] = GraphNode(node1)
            if node2 not in nodes_map:
                nodes_map[node2] = GraphNode(node2)
            nodes_map[node2].add_neighbour(nodes_map[node1])
            nodes_map[node1].add_neighbour(nodes_map[node2])
        
        leaf_deque = collections.deque([])
        for node in nodes_map:
            if nodes_map[node].is_leaf():
                leaf_deque.append(nodes_map[node])
        
        while n>2:
            curr_len = len(leaf_deque)
            n -= curr_len
            
            for _ in range(curr_len):
                curr_node = leaf_deque.popleft()
                for neighbour in curr_node.neighbours:
                    neighbour.remove_neighbour(curr_node)
                    if neighbour.is_leaf():
                        leaf_deque.append(neighbour)
        return [node.value for node in leaf_deque]
                
                
            