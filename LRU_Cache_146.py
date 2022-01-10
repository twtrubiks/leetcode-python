'''
https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

'''

import collections

class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity


    def get(self, key: int) -> int:
        # 假如key存在, 移動到最後(當作是使用過)並回傳, 如果不存在回傳 -1
        if key in self:
            self.move_to_end(key)
            return self[key]
        return -1


    def put(self, key: int, value: int) -> None:
        # 如果 key 存在, 改變 value(並且移到最後),
        # 不存在則加入
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

c = LRUCache(2)
c.put(1,1)
c.put(2,2)
c.get(1)
c.put(3,3)
print(c)
c.put(4,4)
print(c)