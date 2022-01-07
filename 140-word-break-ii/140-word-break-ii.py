class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        sol = []
        queue = collections.deque([(0, [])])        
        while queue:
            start, words = queue.pop()
            if start == len(s):
                sol.append(' '.join(words))
                continue
            for end in range(start, len(s)):
                if s[start:end+1] in word_set:
                    queue.append((end+1, words+[s[start:end+1]]))
        return sol
                    