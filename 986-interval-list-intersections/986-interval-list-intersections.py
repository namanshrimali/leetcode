class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_ptr, second_ptr = 0, 0
        sol = []
        while(first_ptr < len(firstList) and second_ptr < len(secondList)):
            first_start, first_end = firstList[first_ptr]
            second_start, second_end = secondList[second_ptr]
            if first_end < second_start:
                first_ptr+=1
                continue
            elif second_end < first_start:
                second_ptr+=1
                continue
            
            sol_start = max(first_start, second_start)
            sol_end = min(first_end, second_end)
            
            if sol_end == first_end:
                first_ptr+=1
            else:
                second_ptr+=1
            sol.append([sol_start, sol_end])
        return sol
                