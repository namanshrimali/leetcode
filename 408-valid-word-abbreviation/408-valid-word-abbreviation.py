class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while(i<len(abbr)):
            if abbr[i].isdigit():
                # returning 0 as starts with 0
                if abbr[i] == '0':
                    return False
                # calculating num
                num = int(abbr[i])
                while(i+1<len(abbr) and abbr[i+1].isdigit()):
                    num = 10*num+int(abbr[i+1])
                    i+=1
                # if num exceeds size of word
                if j+num-1 >= len(word):
                    return False
                j+=num-1
            else:
                if j >= len(word) or abbr[i] != word[j]:
                    return False
            i+=1
            j+=1
        return True if j == len(word) else False