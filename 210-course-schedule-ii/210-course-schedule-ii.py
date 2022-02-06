class Solution:
    WHITE = 0
    GRAY = 1
    BLACK = 2
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        node_ref, colour = {}, {}
        if numCourses == 1:
            return [numCourses-1]
        sol, is_cyclic = [], False
        # graph data structure. If cycle detected, return empty array
        
        for course, prereq in prerequisites:
            node_ref[prereq] = node_ref.get(prereq, [])
            node_ref[prereq].append(course)
        
        def dfs(node):
            nonlocal is_cyclic
            if is_cyclic:
                return
            colour[node] = Solution.GRAY
            
            if node in node_ref:
                for child in node_ref[node]:
                    if child in colour and colour[child]==Solution.GRAY:
                        is_cyclic = True
                        return
                    elif child not in colour or colour[child]==Solution.WHITE:
                        dfs(child)
            colour[node] = Solution.BLACK
            sol.append(node)
        for vertex in range(numCourses):
            if vertex not in colour or colour[vertex] == Solution.WHITE:
                dfs(vertex)
        return [] if is_cyclic else sol[::-1] 