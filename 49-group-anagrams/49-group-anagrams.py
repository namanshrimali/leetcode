class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_dict = {}
        for word in strs:
            letter_count = [0]*26
            for letter in word:
                letter_count[ord(letter)-ord('a')]+=1
            letter_count = tuple(letter_count)
            if letter_count in char_dict:
                char_dict[letter_count].append(word)
            else:
                char_dict[letter_count] = [word]
        return list(char_dict.values())
                
        