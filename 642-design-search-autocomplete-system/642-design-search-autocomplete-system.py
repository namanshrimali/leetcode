class TrieNode:
    def __init__(self, sentence=None):
        self.children = {}
        self.sentence = sentence
        self.hot = 0
        self.is_end = False

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = TrieNode()
        self.last_node = self.trie
        self.curr_sentence = []
        self.curr_not_found = False
        
        for i in range(len(sentences)):
            self.add_on_trie(sentences[i], times[i])
            
    def add_on_trie(self, sentence, hot):
        root = self.trie
        
        for char in sentence:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.sentence = sentence
        root.hot -= hot
        root.is_end = True
        
    def input(self, c: str) -> List[str]:
        def dfs(node):
            nonlocal res
            if node.is_end:
                res.append((node.hot, node.sentence))
            for children in node.children:
                dfs(node.children[children])
        if c == '#':
            self.add_on_trie(''.join(self.curr_sentence), 1)
            self.curr_sentence = []
            self.last_node = self.trie
            self.curr_not_found = False
            return []
        self.curr_sentence.append(c)
        if self.curr_not_found:
            return []
        if c in self.last_node.children:
            self.last_node = self.last_node.children[c]
            res = []
            dfs(self.last_node)
            return [sentence for _, sentence in sorted(res)][:3]
        self.curr_not_found = True
        return []


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)