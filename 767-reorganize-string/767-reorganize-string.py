class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        counter_map = {}
        for char in s:
            counter_map[char] = counter_map.get(char, 0) + 1
        for char in counter_map:
            heapq.heappush(heap, (-counter_map[char], char))
        answer = []
        while heap:
            freq, top_ele = heapq.heappop(heap)
            if heap:
                second_freq, second_ele = heapq.heappop(heap)
                answer.append(top_ele)
                answer.append(second_ele)
                freq += 1
                second_freq += 1
                if second_freq:
                    heapq.heappush(heap, (second_freq, second_ele))
                if freq:
                    heapq.heappush(heap, (freq, top_ele))
            else:
                if freq < -1:
                    return ""
                else:
                    answer.append(top_ele)
        return ''.join(answer)