# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        total_rows, total_cols = binaryMatrix.dimensions()
        
        def get_leftmost_one(row_idx, col_idx):
            start, end = 0, col_idx
            
            while start < end:
                mid = (start+end)//2
                if binaryMatrix.get(row_idx, mid) == 0:
                    start = mid+1
                else:
                    end = mid
            return end
        
        leftmost = total_cols
        for row in range(total_rows):
            leftmost = get_leftmost_one(row, leftmost)
            
        return -1 if leftmost==total_cols else leftmost