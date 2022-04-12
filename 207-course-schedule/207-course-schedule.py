class Course:
    def __init__(self):
        self.children = set()
        self.parent = set()
    
    def add_prereq(self, parent):
        self.parent.add(parent)
    
    def remove_prereq(self, parent):
        self.parent.remove(parent)
    
    def add_follow_up(self, child):
        self.children.add(child)
    
    def remove_follow_up(self, child):
        self.children.remove(child)
    def has_no_prereq(self):
        return len(self.parent) == 0
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses : List[Course] = [Course() for _ in range(numCourses)]
        
        for prereq, followup in prerequisites:
            courses[prereq].add_follow_up(courses[followup])
            courses[followup].add_prereq(courses[prereq])
        
        deque = collections.deque([])
        for course in courses:
            if course.has_no_prereq():
                deque.append(course)
        
        while deque and numCourses:
            course = deque.popleft()
            for followup in course.children:
                followup.remove_prereq(course)
                if followup.has_no_prereq():
                    deque.append(followup)
            numCourses -=1
        
        return False if numCourses > 0 else True
                    