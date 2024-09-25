

class LFUCache:

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.freq_dict = {}
        self.min_freq = 0
        self.freq_key_mapping = {}

    
    def get(self, key):
        if key not in self.cache:
            return None
        else:
            self.update_freq(key)
            return self.cache[key]

    
    
    def insert(self, key, value):
        if key in self.cache:
            self.update_freq(key)
            self.cache = value
        else:
            if len(self.cache) == self.capacity:
                self.remove_key()
            self.cache[key] = value
            self.freq_dict[key] = 1
            if 1 not in self.freq_key_mapping:
               self.freq_key_mapping[1] = []
            self.freq_key_mapping[1].append(key)
            self.min_freq = 1
            # print(f"min is {self.min_freq}")
        


    
    def update_freq(self, key):
        freq = self.freq_dict[key]
        self.freq_key_mapping[freq].remove(key)
        if not self.freq_key_mapping[freq]:
            del self.freq_key_mapping[freq]
            if freq == self.min_freq:
              self.min_freq += 1
        new_freq = freq+1
        if new_freq not in self.freq_key_mapping:
            self.freq_key_mapping[new_freq] = []
        self.freq_key_mapping[new_freq].append(key)
        self.freq_dict[key] +=1

       

    
    def remove_key(self):
        min_freq = self.min_freq
        print(min_freq)
        key_to_be_removed = self.freq_key_mapping[min_freq].pop(0)
        if not self.freq_key_mapping[key_to_be_removed]:
            del self.freq_key_mapping[key_to_be_removed]
        del self.cache[key_to_be_removed]
        del self.freq_dict[key_to_be_removed]




lfu =LFUCache(3)

print(lfu.get(4))

lfu.insert(1, 4)
print(lfu.get(1))

lfu.insert(2,3)
lfu.insert(3,4)
print(lfu.get(3))
lfu.insert(4,1)
print(lfu.get(2))


        

        

