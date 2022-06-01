def get_char_idx(char):
    return ord(char)-ord('a')

def get_char_from_idx(idx):
    return chr(idx + ord('a'))

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_word = False

    def add_word(self, word):
        curr_node = self
        for char in word:
            idx = get_char_idx(char)
            if curr_node.children[idx] is None:
                curr_node.children[idx] = TrieNode()
            curr_node = curr_node.children[idx]
        curr_node.is_word = True
    
    def get_top_three_words(self, word_array, top_three_words = []):
        if len(top_three_words) == 3:
            return top_three_words
        if self.is_word:
            top_three_words.append(''.join(word_array))
            
        for i in range(len(self.children)):
            if self.children[i] is not None:
                top_three_words = self.children[i].get_top_three_words(word_array + [get_char_from_idx(i)], top_three_words)
        return top_three_words
                    
            
            
            
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        
        for product in products:
            root.add_word(product)
        
        result = []
        curr_node = root
        i = 0
        while i < len(searchWord):
            idx = get_char_idx(searchWord[i])
            if curr_node.children[idx] is None:
                break
            curr_node = curr_node.children[idx]
            result.append(curr_node.get_top_three_words([searchWord[:i+1]], []))
            i+=1
            
        for j in range(i, len(searchWord)):
            result.append([])
        
        return result
