class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a:
            heapq.heappush(heap, (-a, 'a'))
        if b:
            heapq.heappush(heap, (-b, 'b'))
        if c:
            heapq.heappush(heap, (-c, 'c'))
        sol = []
        while heap:
            top_freq, top_letter = heapq.heappop(heap)
            if len(sol) >=2 and sol[-2]==sol[-1]==top_letter:
                if len(heap) == 0:
                    break
                second_freq, second_letter = heapq.heappop(heap)
                sol.append(second_letter)
                second_freq += 1
                if second_freq:
                    heapq.heappush(heap, (second_freq, second_letter))
            else:
                sol.append(top_letter)
                top_freq += 1
            if top_freq:
                heapq.heappush(heap, (top_freq, top_letter))
        
        return ''.join(sol)
        