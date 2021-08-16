class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1).'''
        hash_v = self.horner_hash(key)
        if self.in_table(key):        
            if self.hash_table[hash_v][0] == key: self.hash_table[hash_v][1] = value 
            else: # else collision
                for j in range(1, self.table_size):
                    new_hash = hash_v + j**2 # calculating new hash using quadratic probing
                    if self.hash_table[new_hash][0] == key: 
                        self.hash_table[new_hash][1] = value 
                        break
        else:
            self.num_items += 1
            if self.get_load_factor() > 0.5:
                self.rehash()
                hash_v = self.horner_hash(key) # we need to get the new hash value after rehashing
            if self.hash_table[hash_v] == None: self.hash_table[hash_v] = [key, value]
            else: # else collision
                for j in range(1, self.table_size):
                    new_hash = hash_v + j**2 # calculating new hash using quadratic probing          
                    if self.hash_table[new_hash] == None: 
                        self.hash_table[new_hash] = [key, value]
                        break
                
    def horner_hash(self, key):
        ''' Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification.'''
        g = 31
        hash_v = 0
        for i in range(len(key)):
            hash_v = g * hash_v + ord(key[i])
        hash_v = hash_v % self.table_size
        return hash_v

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash_v table, False otherwise.'''
        hash_v = self.horner_hash(key)
        if self.hash_table[hash_v] != None and self.hash_table[hash_v][0] == key: return True
        else:
            for j in range(1, self.table_size):
                new_hash = hash_v + j**2 # quadratic probing if hash collides...
                if new_hash >= self.table_size or self.hash_table[new_hash] == None: return False 
                if self.hash_table[new_hash][0] == key: return True
            
    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        if self.in_table(key):
            hash_v = self.horner_hash(key)
            if self.hash_table[hash_v][0] == key: return hash_v
            else:
                for j in range(1, self.table_size):
                    new_hash = hash_v + j**2 # quadratic probing if hash collides...
                    if self.hash_table[new_hash][0] == key: return new_hash
        return None

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        keys = []
        for keyVal in self.hash_table:
            if keyVal != None:
                keys.append(keyVal[0])
        return keys

    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        if self.in_table(key):
            index = self.get_index(key)
            return self.hash_table[index][1]
        return None

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.num_items/self.table_size

    # Helper functions
    def rehash(self):
        # grab all key value pairs from hash table
        keys = self.get_all_keys()
        keyVals = []
        for i in range(len(keys)):
            index = self.get_index(keys[i])
            keyVals.append([keys[i], self.hash_table[index][1]])

        # increase size of hash table and reset/update hash table
        self.table_size = self.table_size *2 + 1
        self.hash_table = [None]*self.table_size

        # insert into updated hash table
        for key, value in keyVals: # unpacking a list
            self.insert(key, value)
        


            
        
