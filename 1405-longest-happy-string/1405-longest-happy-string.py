class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a>0:
            heapq.heappush(heap, (-a, 'a'))
        if b>0:
            heapq.heappush(heap, (-b, 'b'))
        if c>0:
            heapq.heappush(heap, (-c, 'c'))
        sol = []
        while heap:
            max_ele, max_char = heapq.heappop(heap)
            if len(sol)>1 and sol[-2] == sol[-1] == max_char:
                if not heap:
                    break
                else:
                    second_max_ele, second_max_char = heapq.heappop(heap)
                    sol.append(second_max_char)
                    second_max_ele += 1
                    
                    if second_max_ele != 0:
                        heapq.heappush(heap, (second_max_ele, second_max_char))
                    heapq.heappush(heap, (max_ele, max_char))
            else:
                sol.append(max_char)
                max_ele += 1

                if max_ele != 0:
                    heapq.heappush(heap, (max_ele, max_char))
        return ''.join(sol)