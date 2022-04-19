class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        process_tree = {}
        n = len(pid)
        for i in range(n):
            if pid[i] not in process_tree:
                process_tree[pid[i]] = set()
            if ppid[i] !=0:
                if ppid[i] not in process_tree:
                    process_tree[ppid[i]] = set()
                process_tree[ppid[i]].add(pid[i])

        deque = collections.deque([kill])
        killed_processes = set()
        while deque:
            process = deque.popleft()
            killed_processes.add(process)
            
            for child in process_tree[process]:
                if child not in killed_processes:
                    deque.append(child)
        
        return killed_processes