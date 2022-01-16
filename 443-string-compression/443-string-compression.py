class Solution:
    def compress(self, chars: List[str]) -> int:            
        last_char, char_count, L = chars.pop(0), 1, len(chars)
        for i in range(L):
            curr_char = chars.pop(0)
            if curr_char == last_char:
                char_count+=1
            else:
                # appending last_char
                chars.append(last_char)
                if char_count > 1:
                    chars+=list(str(char_count))
                last_char = curr_char
                char_count = 1
        chars.append(last_char)
        if char_count > 1:
            chars+=list(str(char_count))        
        return len(chars)
                
        