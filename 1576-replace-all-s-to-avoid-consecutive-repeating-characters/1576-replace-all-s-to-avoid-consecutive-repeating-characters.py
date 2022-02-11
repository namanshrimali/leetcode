class Solution:
    def modifyString(self, s: str) -> str:
        alphabet = 'abcdefghjklmnopqrstuvwxyz'
        s = list(s)
        for i in range(len(s)):
            if s[i] == '?':
                invalid = set()
                if i-1>-1:
                    invalid.add(s[i-1])
                if i+1<len(s):
                    invalid.add(s[i+1])
                for letter in alphabet:
                    if letter not in invalid:
                        s[i] = letter
                        break
        return ''.join(s)
        