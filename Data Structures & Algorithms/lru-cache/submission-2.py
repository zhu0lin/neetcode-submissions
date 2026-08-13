from collections import deque
class LRUCache:
    """
    Understand
    In the start, we'll initialize a cache of size capacity

    When we want to put a new key in, we are replacing the value of the key
    if it already exists in the cache. If it doesn't exist, add the key-value pair
    to the cache. This is alright if the len(cache) < capacity. But if
    cache == capacity, we need to pop off the least recently used key
    and add this new key-value pair to the cache.

    When we want to get a key, we return the value corresponding to it.
    If the key doesn't exist, return -1.

    I think the main two things to figure out is.
    1. This kinda goes with the 2nd concern. How can we represent our
    cache so that we are able to find the least recently used key?
    2. How do we know which one is the least recently used key in the cache

    I think the answer to the first concern should be: 
    the key-value pairs should be a dictionary. this just makes the most
    sense for easy O(1) lookups.
    as for the "least recently used" cache. we should maybe use a deque?
    and pop from the left, fifo
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.cache = deque()

    def get(self, key: int) -> int:
        if key in self.dict:
            self.cache.remove(key)
            self.cache.append(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
            self.cache.remove(key)
            self.cache.append(key)
            return
        if len(self.dict) == self.capacity:
            popped = self.cache.popleft()
            del self.dict[popped]
            
        self.dict[key] = value
        self.cache.append(key)
