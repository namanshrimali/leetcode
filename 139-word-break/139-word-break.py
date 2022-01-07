class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set, visited = set(wordDict), set()
        queue = collections.deque([0])
        while queue:
            start = queue.popleft()
            if start == len(s):
                return True
            if start in visited:
                continue
            for end in range(start+1, len(s)+1):
                if s[start:end] in word_set:
                    queue.append(end)
            visited.add(start)
        return False
            