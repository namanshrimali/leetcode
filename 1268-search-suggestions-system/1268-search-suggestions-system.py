def get_index(char):
    return ord(char) - ord('a')

class Node:    
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_word = False
    
    def add_word(self, word):
        node = self
        for char in word:
            idx = get_index(char)
            if node.children[idx] is None:
                node.children[idx] = Node()
            node = node.children[idx]
        node.is_word = True
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        end_result = []
        
        def dfs(node, word):
            nonlocal top_matching
            
            if len(top_matching) == 3:
                return
            
            if node.is_word:
                top_matching.append(word)
            
            for i in range(26):
                if node.children[i] != None:
                    dfs(node.children[i], word+chr(ord('a') + i))
            
        
        root = Node()
        for product in products:
            root.add_word(product)
        
        node = root
        
        for i, letter in enumerate(searchWord):
            idx = get_index(letter)
            node = node.children[idx]
            
            if node == None:
                for j in range(len(searchWord)-i):
                    end_result.append([])
                break
            
            top_matching = []
            dfs(node, searchWord[:i+1])
            end_result.append(top_matching[:3])
    
        return end_result
            
        
        