class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        counter_hash_map = {}
        for letter in s:
            counter_hash_map[letter] = counter_hash_map.get(letter, 0)+1
        for key in counter_hash_map:
            heapq.heappush(heap, [-counter_hash_map[key], key])
        sol = []
        while heap:
            freq, top_letter = heapq.heappop(heap)
            if sol and sol[-1] == top_letter:
                if heap:
                    second_freq, second_top = heapq.heappop(heap)
                    second_freq+=1
                    sol.append(second_top)
                    if second_freq!=0:
                        heapq.heappush(heap, [second_freq, second_top])
                else:
                    return ''
            else:
                freq+=1
                sol.append(top_letter)
            if freq != 0:
                heapq.heappush(heap, [freq, top_letter])
        return ''.join(sol)
        