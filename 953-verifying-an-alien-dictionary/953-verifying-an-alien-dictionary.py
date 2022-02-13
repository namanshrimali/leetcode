class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        order_dict = {}
        
        for i in range(len(order)):
            order_dict[order[i]] = i

        def are_words_sorted(word1, word2):
            idx = 0
            while idx<len(word1) and idx<len(word2):
                if order_dict[word1[idx]] < order_dict[word2[idx]]:
                    return True
                elif order_dict[word1[idx]] > order_dict[word2[idx]]:
                    return False
                idx+=1
            return True if idx == len(word1) else False
        
        for i in range(1, len(words)):
            if are_words_sorted(words[i-1], words[i]):
                continue
            return False
        return True