class Node:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_word = False
    
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        curr = self.root
        for char in word:
            char_idx = ord(char) - ord('a')
            
            if curr.children[char_idx] is None:
                curr.children[char_idx] = Node()
            curr = curr.children[char_idx]
        curr.is_word = True
    
        
    def get_word_starting_with(self, prefix):
        def dfs(curr, word):
            nonlocal answer
            if len(answer) == 3:
                return
            if curr.is_word:
                answer.append(word)

            for i in range(26):
                if curr.children[i] != None:
                    dfs(curr.children[i], word+chr(ord('a')+i))
        
        curr = self.root
        answer = []
        for char in prefix:
            char_idx = ord(char)-ord('a')
            if curr.children[char_idx] == None:
                return answer
            curr = curr.children[char_idx]
        dfs(curr, prefix)
        return answer
                
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        result = []
        for product in products:
            trie.insert(product)
        for i in range(len(searchWord)):
            result.append(trie.get_word_starting_with(searchWord[:i+1]))
        return result
        