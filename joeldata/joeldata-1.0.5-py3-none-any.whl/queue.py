#FastQueue is O(1), Queue has O(N) dequeue performance.1

"""
First-in First-Out

Examples:
* print queue
"""

# back --> [1, 2, 3] <-- front

def lst_to_string(lst):
    string=''
    if len(lst)==1:
        return str(lst[0])
    if len(lst)>=2:
        for i, num in enumerate(lst):
            if i==len(lst)-1: #last item, so include 'and' and no comma at end
                string+=f'and {num}'
            else: #comma between items
                string+=f'{num}, '
        string+='.'
    
    return string

class MemQueue: #basic
    def __init__(self, *args):
        self.data=[]
        for item in args:
            self.data.append(item)
    
    def enqueue(self, val) -> None:
        self.data.append(val)
    
    def dequeue(self):
        return self.data.pop(0) #returns number
    
    def peek(self):
        return self.data[0]
    
    def is_empty(self) -> bool:
        return self.data==[]

    def __str__(self):
        return 'MemQueue: '+lst_to_string(self.data)

class FastQueue: #faster, O(1) operations
    def __init__(self, *args):
        self.data=[]
        for item in args:
            self.data.append(item)
        self.front=0
    
    def enqueue(self, val) -> None:
        self.data.append(val)
    
    def dequeue(self): #returns removed element
        item=self.data[self.front]
        self.front+=1
        return item
    
    def peek(self):
        return self.data[self.front]
    
    def is_empty(self) -> bool:
        return (len(self.data)-self.front)==0

    def __str__(self):
        return 'FastQueue: '+lst_to_string(self.data[self.front:])

class Queue: #compromise between MemQueue and FastQueue
    # Never takes up more than 10% of list size or use up more space than neeeded

    def __init__(self, *args):
        self.data=[]
        for item in args:
            self.data.append(item)
        self.front=0

    def __iter__(self):
        return iter(self.data[self.front:])
    
    def enqueue(self, val) -> None:
        self.data.append(val)
    
    def dequeue(self): #returns removed element
        item=self.data[self.front]
        self.front+=1
        # O(N)/O(1/N) is O(1)
        if self.front>=len(self.data)*.1: #When 10% of list, reallocates memory
            self.realloc()
        return item
    
    def realloc(self): #sets front to zero, and reallocates memory
        self.data=self.data[self.front:]
        self.front=0
    
    def peek(self):
        return self.data[self.front]
    
    def is_empty(self) -> bool:
        return (len(self.data)-self.front)==0

    def __str__(self):
        return 'Queue: '+lst_to_string(self.data[self.front:])
    
    def __len__(self):
        return len(self.data)
    
    def to_list(self): #see the list
        return self.data
