class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList:
            return 0
        word_set = set(wordList) 
        
        if endWord not in word_set:
            return 0
        
        A_LETTER_ASCII = ord('a')
        
        def next_words(word):            
            for idx, curr_letter in enumerate(word):
                curr_letter_idx = ord(curr_letter) - A_LETTER_ASCII
                for next_letter_idx in range(26):
                    if next_letter_idx != curr_letter_idx:
                        yield word[:idx] + chr(next_letter_idx + A_LETTER_ASCII) + word[idx+1:]
        
        shortest_len = float('inf')
        visited = set([beginWord])
        curr_len = 0
        word_queue = collections.deque([beginWord])
        
        while word_queue:
            curr_len += 1
            curr_queue_len = len(word_queue)
            for _ in range(curr_queue_len):
                curr_word = word_queue.popleft()
                
                if curr_word == endWord:
                    shortest_len = min(shortest_len, curr_len)
                    return curr_len
                for next_word in next_words(curr_word):
                    if next_word in word_set and next_word not in visited:
                        word_queue.append(next_word)
                        visited.add(next_word)
        
        return 0