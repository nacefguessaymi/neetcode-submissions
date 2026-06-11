class MyHashSet:

    def __init__(self):
        self.has_set = set()

    def add(self, key: int) -> None:
        self.has_set.add(key)

    def remove(self, key: int) -> None:
        if MyHashSet.contains(self, key):
            self.has_set.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.has_set


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)