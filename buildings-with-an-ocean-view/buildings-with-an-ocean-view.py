class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        sol = [] # this will be the array which will store our solution
        max_height = 0 # this will be the max height of the building from right
        for i in range(len(heights)-1, -1, -1): # iterating from right to left
            if heights[i] > max_height:         # checking if the current height is greater than biggest building on the right
                sol.append(i)
                max_height = heights[i]         # updating max_height variable
        return sol[::-1]        # reversing the soolution array since we traversed from right to left
    
# Space Complexity : O(1)
# Time complexity : O(n)