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
        lowest_col_idx = dimensions[1]
        for row in range(dimensions[0]):
            l = 0
            while(l<lowest_col_idx):
                mid = (l+lowest_col_idx)//2
                if binaryMatrix.get(row, mid) == 1:
                    lowest_col_idx = mid
                else:
                    l = mid+1
        return -1 if lowest_col_idx == dimensions[1] else lowest_col_idx
        
            
