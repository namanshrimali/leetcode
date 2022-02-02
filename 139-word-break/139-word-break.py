class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited, queue = set(), collections.deque([0])
        L = len(s)
        while queue:
            start = queue.popleft()
            if start in visited:
                continue
            if start == L:
                return True
            for end in range(start, L):
                if s[start:end+1] in wordDict:
                    queue.append(end+1)
            visited.add(start)
        return False
        