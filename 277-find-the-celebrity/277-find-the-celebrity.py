# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate_celebrity = 0
        for curr in range(1, n):
            if knows(candidate_celebrity, curr):
                # candidate is not a celebrity
                candidate_celebrity = curr
        
        # we've our candidate celebrity, now we'll check whether everyone knows him and make sure
        # candidate doesn't know anyone
        for i in range(n):
            if i == candidate_celebrity:
                continue
            if not(knows(i, candidate_celebrity) and not knows(candidate_celebrity, i)):
                return -1
        return candidate_celebrity