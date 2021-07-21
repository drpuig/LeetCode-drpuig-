from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = dict()
        self.deq = deque()

    def get(self, key: int) -> int:
        if key in self.hash:
            value = self.hash[key]
            self.deq.remove(key)
            self.deq.append(key)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hash:
            if len(self.deq) == self.capacity:
                oldest = self.deq.popleft()
                del self.hash[oldest]
        else: 
            self.deq.remove(key)
        self.hash[key] = value
        self.deq.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)