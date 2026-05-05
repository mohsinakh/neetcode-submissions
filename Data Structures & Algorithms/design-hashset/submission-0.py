class MyHashSet:

    def __init__(self):
        self.data = {}

    def add(self, key: int) -> None:
        if key in self.data:
            self.data[key] += 1
        else:
            self.data[key] = 0
    def remove(self, key: int) -> None:
        if key in self.data:
            self.data[key] = -1


    def contains(self, key: int) -> bool:
        if key in self.data and self.data[key]!=-1:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)