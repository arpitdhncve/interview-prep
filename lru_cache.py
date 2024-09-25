from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity:int):
        self.cache = OrderedDict()
        self.capacity = capacity


    def get(self, key):
        if key not in self.cache:
            print("Data doesn't exist")
            return None
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    

    def insert(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)





cache = LRUCache(2)
cache.insert("key1", "value1")
cache.insert(1, "qwerty")
print(cache.get(1))
cache.get("key2")
cache.insert(2, "value2")
cache.get("key1")


