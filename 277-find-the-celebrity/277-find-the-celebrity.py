# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity_candidate = 0
        for i in range(1, n):
            if knows(celebrity_candidate, i):
                # celebrity_candidate is not a celebrity, but i might be
                celebrity_candidate = i
        for i in range(n):
            if i == celebrity_candidate:
                continue
            if knows(celebrity_candidate, i) or not knows(i, celebrity_candidate):
                # either celebrity_candidate knows i or i does not know celebrity_candidate
                return -1
        return celebrity_candidate
                
        