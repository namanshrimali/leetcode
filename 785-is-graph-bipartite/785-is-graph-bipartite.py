class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 1 is red, -1 is blue
        colour = {}
        for node in range(len(graph)):
            if node in colour:
                continue
            colour[node] = 1
            stack = [node]
            while stack:
                curr_node = stack.pop()
                for neighbour in graph[curr_node]:
                    if neighbour not in colour:
                        stack.append(neighbour)
                        colour[neighbour] = -colour[curr_node]
                    elif colour[neighbour] == colour[curr_node]:
                        return False
        return True
                