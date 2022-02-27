class Solution:
    def minDeletions(self, s: str) -> int:
        letter_count = [0]*26
        
        def letter_index(letter):
            return ord(letter)-ord('a')
        
        for letter in s:
            letter_count[letter_index(letter)]+=1
        
        letter_count.sort(reverse = True)
        
        answer = 0
        print(letter_count)
        seen = set()
        for i in range(len(letter_count)):
            if letter_count[i] == 0:
                break
            while letter_count[i] in seen and letter_count[i] != 0:
                letter_count[i]-=1
                answer+=1
            seen.add(letter_count[i])
        return answer
            