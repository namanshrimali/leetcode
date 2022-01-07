"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return
        node_map = {}
        queue = collections.deque([node])
        while queue:
            graph_node = queue.popleft()
            node_map[graph_node] = Node(graph_node.val, [])
            for neighbor in graph_node.neighbors:
                if neighbor not in node_map:
                    queue.append(neighbor)
        for graph_node in node_map:
            for neighbor in graph_node.neighbors:
                node_map[graph_node].neighbors.append(node_map[neighbor])
        return node_map[node]
        