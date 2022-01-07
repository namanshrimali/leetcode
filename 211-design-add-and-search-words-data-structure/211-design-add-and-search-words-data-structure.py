class WordDictionary:

    def __init__(self):
        self.trie = {}
        
    def _add_on_level(self, word, level):
        if word == '':
            level['#'] = {}
            return
        if word[0] not in level:
            level[word[0]] = {}

        self._add_on_level(word[1:], level[word[0]])
        
    def addWord(self, word: str) -> None:
        self._add_on_level(word, self.trie)
        
    def _search_on_level(self, word, level):
        if word == '':
            if '#' in level:
                return True
            else:
                return False
        
        if word[0] == '.':
            found = False
            for start_letter in level:
                found = self._search_on_level(word[1:], level[start_letter])
                if found:
                    break
            return found
        else:
            if word[0] not in level:
                return False
            return self._search_on_level(word[1:], level[word[0]])
            
        
    def search(self, word: str) -> bool:
        return self._search_on_level(word, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)