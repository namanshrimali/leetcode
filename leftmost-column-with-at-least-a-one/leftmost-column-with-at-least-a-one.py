# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dimensions = binaryMatrix.dimensions()
        sol = -1
        l, r = 0, dimensions[1]-1
        while(l<=r):
            mid = (l+r)//2
            found = False
            for i in range(dimensions[0]):
                if binaryMatrix.get(i, mid) == 1:
                    found = True
                    break
            if found:
                sol = mid
                r = mid-1
            else:
                l=mid+1
        return sol
            