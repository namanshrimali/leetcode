class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        L = len(pid)
        parent_child_map = {}
        for i in range(L):
            if ppid[i] in parent_child_map:
                parent_child_map[ppid[i]].append(pid[i])
            else:
                parent_child_map[ppid[i]] = [pid[i]]
        if kill in parent_child_map:
            deque = collections.deque([kill])
            killed = set()
            while deque:
                parent_task = deque.popleft()
                killed.add(parent_task)
                for child in parent_child_map.get(parent_task, []):
                    deque.append(child)
            return list(killed)
        else:
            return [kill]