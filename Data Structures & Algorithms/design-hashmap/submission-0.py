class MyHashMap:

    def __init__(self):
        self.h_map= dict()

    def put(self, key: int, value: int) -> None:
        
        self.h_map[key]=value

    def get(self, key: int) -> int:
        if key in self.h_map:
            return self.h_map[key]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if key in self.h_map:
            del self.h_map[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)