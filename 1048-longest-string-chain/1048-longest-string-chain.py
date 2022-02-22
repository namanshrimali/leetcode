class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        connections_dict = {}
        words.sort(key=len)
        
        def is_connected(word1, word2):
            L1, L2 = len(word1), len(word2)
            if abs(L1-L2) != 1:
                return False
            if L1>L2:
                for i in range(L1):
                    if word1[0:i]+word1[i+1:L1] == word2:
                        return True
            else:
                for i in range(L2):
                    if word2[0:i]+word2[i+1:L2] == word1:
                        return True
            return False
        
        for word in words:
            if word in connections_dict:
                continue
            connections_dict[word] = [[], None]
            for prev_word in connections_dict:
                if is_connected(prev_word, word):
                    connections_dict[word][0].append(prev_word)
        sol = 0
        
        def dfs(letter):
            nonlocal sol
            if connections_dict[letter][1] !=  None:
                return connections_dict[letter][1]
            total_connected = 1
            for connected in connections_dict[letter][0]:
                total_connected = max(total_connected, 1+dfs(connected))
            sol = max(sol, total_connected)
            connections_dict[letter][1] = total_connected
            return total_connected
        
        for word in words:
            dfs(word)
        return sol
        
        