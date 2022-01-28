class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        output = []
        for word in s:
            if word == '':
                continue
            output.append(word)
        print(output)
        return ' '.join(output[::-1])
        