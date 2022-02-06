class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        child_ref, indegree = {}, {}
        for course, prereq in prerequisites:
            child_ref[prereq] = child_ref.get(prereq, [])
            child_ref[prereq].append(course)
            indegree[course] = indegree.get(course, 0)+1
        queue = collections.deque([k for k in range(numCourses) if k not in indegree])
        sol = []
        
        while queue:
            vertex = queue.popleft()
            sol.append(vertex)
            if vertex in child_ref:
                for child in child_ref[vertex]:
                    indegree[child]-=1
                
                    if indegree[child]==0:
                        queue.append(child)
        return sol if len(sol) == numCourses else []
            