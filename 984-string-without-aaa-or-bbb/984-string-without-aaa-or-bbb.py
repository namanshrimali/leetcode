class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        total_len = a+b
        sol = []
        heap = [(-a, 'a'), (-b, 'b')]
        heapq.heapify(heap)
        
        while heap:
            top_freq, top_ele = heapq.heappop(heap)
            if len(sol)>=2 and sol[-2] == sol[-1] == top_ele:
                # continuous aaa or bbb
                second_freq, second_ele = heapq.heappop(heap)
                sol.append(second_ele)
                second_freq+=1
                if second_freq:
                    heapq.heappush(heap, (second_freq, second_ele))
                
            else:
                sol.append(top_ele)
                top_freq+=1
            
            if top_freq:
                heapq.heappush(heap, (top_freq, top_ele))
        return ''.join(sol)
        