class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        char_heap = []
        for char in char_count:
            heapq.heappush(char_heap, (-char_count[char], char))
        
        result = []
        
        while char_heap:
            first_char_freq, first_char = heapq.heappop(char_heap)
            if char_heap:
                second_char_freq, second_char = heapq.heappop(char_heap)
                result.append(first_char)
                result.append(second_char)
                first_char_freq += 1
                second_char_freq += 1
                
                if first_char_freq != 0:
                    heapq.heappush(char_heap, (first_char_freq, first_char))
                
                if second_char_freq != 0:
                    heapq.heappush(char_heap, (second_char_freq, second_char))
                
            else:
                if -first_char_freq > 1:
                    return ''
                else:
                    result.append(first_char)
        return ''.join(result)
                