class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:    
        order_map = {}
        for seq_no, letter in enumerate(order):
            order_map[letter] = seq_no
        
        def is_misplaced(word1, word2):
            j = 0
            while j<len(word1) and j<len(word2):
                if word1[j]!=word2[j]:
                    if order_map[word1[j]] > order_map[word2[j]]:
                        return True
                    else:
                        return False
                j+=1
            return False if len(word1) <= len(word2) else True
        
        for k in range (len(words)-1):
            if is_misplaced(words[k], words[k+1]):
                return False
        return True