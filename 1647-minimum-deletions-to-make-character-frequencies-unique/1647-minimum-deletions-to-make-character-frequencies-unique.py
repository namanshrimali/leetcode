class Solution:
    def minDeletions(self, s: str) -> int:
        hash_map = {}
        for letter in s:
            hash_map[letter] = hash_map.get(letter, 0) + 1
        sol, found_freq = 0, set()
        heap = [(hash_map[key]) for key in hash_map]
        # heapq.heapify(heap)
        for freq in heap:
            if freq in found_freq:
                exceed = 0
                while freq >0 and freq in found_freq:
                    freq-=1
                    exceed+=1
                sol += exceed
            found_freq.add(freq)
        return sol