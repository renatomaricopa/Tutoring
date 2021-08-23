class MyHashTable:

    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash_table = [[] for _ in range(self.table_size)]
        self.num_items = 0
        self.num_collisions = 0

    def insert(self, key, item):
        hash_v = key % self.table_size
        if self.hash_table[hash_v] == []: # if empty just append to original list
            self.num_items += 1
            self.hash_table[hash_v].append((key, item))
        else:  # else not empty, replace value at key, or add new key
            found_match = False
            for index, pair in enumerate(self.hash_table[hash_v]):
                if key == pair[0]: # if key and original key match, replace with new item
                    self.hash_table[hash_v][index] = (key, item)
                    found_match = True
                    break
            if found_match: return
            else: # add to our growing list of keys for that hash_value
                self.num_items += 1
                if self.load_factor() > 0.5: self.rehash(key, item) # check if rehash needed first
                else: 
                    self.num_collisions += 1
                    self.hash_table[hash_v].append((key, item))
        
    def get(self, key):
        try: 
            hash_v = key % self.table_size
            for index, pair in enumerate(self.hash_table[hash_v]):
                if key == pair[0]: # if key and original key match, return the value
                    return self.hash_table[hash_v][index]
            raise LookupError # if not found we have to raise error
        except LookupError:
            return "Lookup Error"

    def remove(self, key):
        try:
            hash_v = key % self.table_size
            for index, pair in enumerate(self.hash_table[hash_v]):
                if key == pair[0]: # if key and original key match, return the value
                    self.num_items -= 1
                    return self.hash_table[hash_v].pop(index)
            raise LookupError # if not found we have to raise error
        except LookupError:
            return "Lookup Error"
    
    def size(self):
        return self.num_items 
    
    def load_factor(self):
        return self.num_items/self.table_size
    
    def collisions(self):
        return self.num_collisions

    def rehash(self, key, item):
        print(f"Rehashed on key:{key}, and item:{item}")
        old_hash_table = self.hash_table
        self.table_size = self.table_size * 2 + 1
        self.hash_table = [[] for _ in range(self.table_size)]
        self.num_items = 0
        self.insert(key, item) # add new key first 
        for l in old_hash_table: # add everything else from our old hash table
            if l:
                for pair in l: 
                    self.insert(pair[0], pair[1])
            





