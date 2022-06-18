class Process:
    def __init__(self, pid, parent = None):
        self.id = pid
        self.parent = parent
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def set_parent(self, parent):
        self.parent = parent
    
    def kill(self):
        killed_ids = [self.id]
        for child in self.children:
            killed_ids += child.kill()
        return killed_ids
    
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        total_processes = len(pid)
        process_map = {}
        
        for i in range(total_processes):
            if pid[i] not in process_map:
                process_map[pid[i]] = Process(pid[i])
            if ppid[i] not in process_map:
                process_map[ppid[i]] = Process(ppid[i])
            child = process_map[pid[i]]
            parent = process_map[ppid[i]]
            
            if parent.id != 0:
                child.set_parent(parent)
                parent.add_child(child)
        
        return process_map[kill].kill()