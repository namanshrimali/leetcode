class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = 0
        sol = []
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > max_height:
                max_height = heights[i]
                sol.append(i)
        return sol[::-1]