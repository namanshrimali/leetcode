class CourseNode:
    def __init__(self, value):
        self.value = value
        self.children = set()
        self.parents = set()
    def does_not_have_prerequisites(self):
        return len(self.parents) == 0

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_nodes = {}
        scheduled_courses = []
        no_prereq_left_queue = collections.deque([])
        
        for course, prereq in prerequisites:
            if course not in course_nodes:
                course_nodes[course] = CourseNode(course)
            if prereq not in course_nodes:
                course_nodes[prereq] = CourseNode(prereq)
            course_nodes[course].parents.add(course_nodes[prereq])
            course_nodes[prereq].children.add(course_nodes[course])
            
        
        for course in range(numCourses):
            if course not in course_nodes or course_nodes[course].does_not_have_prerequisites():
                no_prereq_left_queue.append(course_nodes.get(course, CourseNode(course)))
        
        
        while no_prereq_left_queue:
            parent_course = no_prereq_left_queue.popleft()
            scheduled_courses.append(parent_course.value)
            for child_course in parent_course.children:
                child_course.parents.remove(parent_course)
                if child_course.does_not_have_prerequisites():
                    no_prereq_left_queue.append(child_course)
        return scheduled_courses if len(scheduled_courses) == numCourses else []
            
                