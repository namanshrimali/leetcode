def get_char_from_idx(idx):
    return chr(ord('a') + idx)

def get_idx_of(char):
    return ord(char) - ord('a')

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_word = False
        
    def get_top_three_words(self, word_prefix, top_three_words):
        if len(top_three_words) == 3:
            return top_three_words
        if self.is_word:
            top_three_words.append(''.join(word_prefix))
            
        for i in range(len(self.children)):
            child = self.children[i]
            if child is not None:
                top_three_words = child.get_top_three_words(word_prefix + [get_char_from_idx(i)], top_three_words)
        return top_three_words
        
    def add_product(self, product):
        curr_node = self
        for letter in product:
            letter_idx = get_idx_of(letter)
            if curr_node.children[letter_idx] == None:
                curr_node.children[letter_idx] = TrieNode()
            curr_node = curr_node.children[letter_idx]
        curr_node.is_word = True
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        for product in products:
            root.add_product(product)
        curr_node = root
        answer = []
        for i in range(len(searchWord)):  
            curr_node = curr_node.children[get_idx_of(searchWord[i])]
            if curr_node is None:
                curr_node = TrieNode()
            answer.append(curr_node.get_top_three_words([searchWord[:i+1]], []))
            
        return answer