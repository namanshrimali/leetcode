class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [strs]
        anagram_dict = {}
        
        for word in strs:
            letter_count = [0] * 26
            for letter in word:
                letter_count[ord(letter) - ord('a')] += 1
            letter_count = tuple(letter_count)
            if letter_count not in anagram_dict:
                anagram_dict[letter_count] = []
            anagram_dict[letter_count].append(word)
        return list(anagram_dict.values())
        