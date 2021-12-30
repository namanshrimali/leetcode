class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        found_list = []
        for i in range(len(s)):
            for word in words:
                if s[i:i+len(word)] == word:
                    if found_list and (found_list[-1][1] > i or found_list[-1][1] == i):
                        found_list[-1][1] = max(i+len(word), found_list[-1][1])
                    else:
                        found_list.append([i, i+len(word)])
                    # do something with i and i+len(word)
        sol = []
        prev_end = 0
        while(found_list):
            start, end = found_list.pop(0)
            sol.append(s[prev_end:start])
            sol.append(f"<b>{s[start:end]}</b>")
            prev_end = end
        sol.append(s[prev_end:])
        return ''.join(sol)
        
            