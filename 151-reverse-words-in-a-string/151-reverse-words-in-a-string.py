class Solution:
    def reverseWords(self, s: str) -> str:
        
        def get_word(idx):
            word = []
            while idx < len(s) and s[idx] != ' ':
                word.append(s[idx])
                idx+=1
            return ''.join(word), idx-1
        word_stack = []
        i = 0
        while i < len(s):
            if s[i] != ' ':
                new_word, i = get_word(i)
                word_stack.append(new_word)
            i+=1
        return ' '.join(word_stack[::-1])
        
        