class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = {}
        for letter in s:
            s_dict[letter] = s_dict.get(letter, 0)+1
        for letter in t:
            if letter in s_dict:
                s_dict[letter]-=1
                if s_dict[letter] == 0:
                    del s_dict[letter]
                
        return sum([s_dict[x] for x in s_dict])