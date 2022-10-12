from .hash import hash

class HashTable:
    def __init__(self, **kwargs):
        #number of arrays created in self.data
        self.max_registers=223 #standard
        if 'max_registers' in kwargs: #user can override standard max_registers
            self.max_registers=kwargs['max_registers']

        self.clear()

    def clear(self): #remove all items & create empty arrays
        self.data=[None for i in range(self.max_registers)]

    def get(self, key) -> any: #returns value
        fetched=self.data[hash(key, self.max_registers)]
        if fetched is None: #nothing at that index
            return None
        for i, item in enumerate(fetched):
            if item[0]==key:
                return item[1] #value
        return None

    def set(self, key, value): # Assign to [key, value] if not exists, otherwise append to LinkedList
        hkey=hash(key, self.max_registers)
        if self.data[hkey] is None: #initialize to array if None
            self.data[hkey]=[]

        for i, item in enumerate(self.data[hkey]):
          if item[0]==key: #set to correct value
            self.data[hkey][i]=[key, value] #set original
            return
        #adding new value because not in list
        self.data[hkey].append([key, value])

    def remove(self, key) -> any: #returns the removed value
        to_del=self.get(key)
        target_found=False
        if to_del is not None: #if there is a value to remove
            #remove the valuex
            values=self.data[hash(key, self.max_registers)]
            for i, val in enumerate(values): #index for editing og
                if val[0]==key: #found target
                    target_found=True
                    del self.data[hash(key, self.max_registers)][i] #delete from array
                    if len(self.data[hash(key, self.max_registers)])==0: #list is empty, so replace with None
                        self.data[hash(key, self.max_registers)]=[]
                    break
        if not target_found:
            raise AttributeError(f'This HashMap has no value "{key}"')
        return to_del
  
    def size(self) -> int: #getter
        counter=0
        for groups in self.data: #array | None
            if groups is not None:
                for items in groups:
                    counter+=1
        return counter

    def is_empty(self) -> bool:
        o=True #output
        for arr in self.data: #any key or value triggers to be true
            if arr is not None:
                for pair in arr:
                    if pair[0] is not None or pair[1] is not None:
                        o=False
        return o

    def has(self, key) -> bool: 
        return key in self.keys()
    
    def keys(self) -> list: # returns array of keys
        o=[]
        for arr in self.data:
            if arr is not None:
                for pair in arr:
                    o.append(pair[0])
        return o

    def values(self) -> list: # returns array of values
        o=[]
        for arr in self.data:
            if arr is not None:
                for pair in arr:
                    o.append(pair[1])
        return o

    def inspect(self) -> list: #returns raw self.data for inspection
        return self.data

    def __str__(self): #format like a python array
        isEmpty=True
        string='HashTable {\n' #open brace
        for item_arr in self.data:
            if item_arr is not None: #add every item in {key}: {value}, format
                for item in item_arr:
                  string+=f'\t{item[0]}: {item[1]},\n'
                  isEmpty=False
        string+='}' #close brace
        string=string[0:-3]+string[-2:] #remove last comma (character at index -2)
        
        if isEmpty:
            return '{}'
        return string
