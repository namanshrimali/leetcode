
def get_letter_idx(letter):
    return ord(letter)-ord('a')

def get_letter_from_idx(idx):
    return chr(ord('a') + idx)

class Node:
    def __init__(self, letter):
        self.children = [None]*26
        self.is_word = False
        self.letter = letter
    
    def insert_product(self, product):
        root = self
        for letter in product:
            letter_idx = get_letter_idx(letter)
            if root.children[letter_idx] == None:
                root.children[letter_idx] = Node(get_letter_from_idx(letter_idx))
            root = root.children[letter_idx]
        root.is_word = True
    
    def get_all_products(self, word_till_now):
        products = []
        def dfs(node, word):
            nonlocal products
            if len(products) == 3:
                return
            if node.is_word:
                products.append(word)
            
            for child in node.children:
                if child != None:
                    dfs(child, word + child.letter)
        dfs(self, word_till_now + self.letter)
        return products
                
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Node('')
        for product in products:
            root.insert_product(product)
        answer = []
        for i in range(len(searchWord)):
            letter = searchWord[i]
            root = root.children[get_letter_idx(letter)]
            if root is None:
                while i < len(searchWord):
                    answer.append([])
                    i+=1
                break
            answer.append(root.get_all_products(searchWord[:i]))
        return answer