class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_map = {}
        for task in tasks:
            count_map[task] = count_map.get(task, 0) + 1
        
        task_values = list(count_map.values())
        task_values.sort()
        
        max_task = task_values.pop()
        waiting_slots = (max_task-1)*n
        
        while(waiting_slots >  0 and task_values):
            waiting_slots -= min(max_task-1, task_values.pop())
        
        waiting_slots = max(0, waiting_slots)
        return waiting_slots+len(tasks)