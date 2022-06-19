class DirectoryNode:
    def __init__(self, name, value = -1):
        self.name = name
        self.value = value
        self.subdirectories = {}
    
    def add_subdirectory(self, subdirectory):
        self.subdirectories[subdirectory.name] = subdirectory
        
        
    def find_subdirectory(self, subdirectory):
        return self.subdirectories.get(subdirectory, None)
        
class FileSystem:

    def __init__(self):
        self.root = DirectoryNode('root', -1)

    def createPath(self, path: str, value: int) -> bool:
        curr_node = self.root
        path = path.split("/")
        n = len(path)
        for i in range(n):
            if len(path[i]) == 0:
                continue
            path_node = curr_node.find_subdirectory(path[i])
            if path_node:
                curr_node = path_node
            else:
                if i == n-1:
                    curr_node.add_subdirectory(DirectoryNode(path[i], value))
                    return True
                break
        return False

    def get(self, path: str) -> int:
        curr_node = self.root
        path = path.split("/")
        n = len(path)
        for i in range(n):
            if len(path[i]) == 0:
                continue
            path_node = curr_node.find_subdirectory(path[i])
            if path_node:
                curr_node = path_node
            else:
                return -1
        return curr_node.value
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)