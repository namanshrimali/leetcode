class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_word_count, window_letter_count = {}, {}
        
        for letter in t:
            t_word_count[letter] = t_word_count.get(letter, 0)+1
        
        formed, required = 0, len(t_word_count)
        
        min_sub_str = (float('inf'), None, None)
        start, end = 0, 0
        
        while(end<len(s)):
            character = s[end]
            window_letter_count[character] = window_letter_count.get(character, 0) + 1
            
            if character in t_word_count and t_word_count[character] == window_letter_count[character]:
                formed+=1
            # contract the window until it ceases to be desirable
            while formed == required and start<=end:
                if end-start+1 <  min_sub_str[0]:
                    min_sub_str = (end-start+1, start, end)
                
                character = s[start]
                window_letter_count[character]-=1
                
                if character in t_word_count and window_letter_count[character] < t_word_count[character]:
                    formed-=1
                start+=1
            end+=1
        return "" if min_sub_str[0] == float('inf') else s[min_sub_str[1]: min_sub_str[2]+1]
                
                