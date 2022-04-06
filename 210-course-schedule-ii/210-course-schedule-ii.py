class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def is_node_parent(i):
            return i not in rel_map or len(rel_map[i][0]) == 0

        rel_map = {}
        for course, prereq in prerequisites:
            if course not in rel_map:
                rel_map[course] = [set(), set()]
            if prereq not in rel_map:
                rel_map[prereq] = [set(), set()]
            rel_map[course][0].add(prereq)
            rel_map[prereq][1].add(course)
        
        deque = collections.deque([])
        answer = []
        
        for i in range(numCourses):
            if is_node_parent(i):
                deque.append(i)
        while deque:
            node = deque.popleft()
            answer.append(node)
            for children in rel_map.get(node, [[], []])[1]:
                rel_map[children][0].remove(node)
                if is_node_parent(children):
                    deque.append(children)
        return [] if len(answer) != numCourses else answer
            
        