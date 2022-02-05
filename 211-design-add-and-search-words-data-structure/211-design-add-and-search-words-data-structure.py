class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for letter in word:
            if letter not in trie:
                trie[letter] = {}
            trie = trie[letter]
        trie['$'] = True
                
    def search(self, word: str) -> bool:
        def _search_at_level(word, level):
            for i, letter in enumerate(word):
                if letter in level:
                    level = level[letter]
                else:
                    if letter == '.':
                        for key in level:
                            if key != '$' and _search_at_level(word[i+1:], level[key]):
                                return True
                    return False
            return '$' in level
        return _search_at_level(word, self.trie)
                    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)