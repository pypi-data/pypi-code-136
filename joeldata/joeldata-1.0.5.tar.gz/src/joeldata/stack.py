"""
Stack is last-in first-out (LIFO)

Only access items at end
"""

def lst_to_string(lst):
    str=''
    for i, num in enumerate(lst):
        if i==len(lst)-1: #last item, so include 'and' and no comma at end
            str+=f'and {num}'
        else: #comma between items
            str+=f'{num}, '
    str+='.'
    return str

class Stack:
    def __init__(self):
        self.data=[] #stack starts empty
    
    def __str__(self):
        return 'Stack: '+lst_to_string(self.data)
    
    def push(self, new):
        self.data.append(new)
        return new
    
    def pop(self):
        removed=self.data[-1]
        self.data.pop()
        return removed
    
    def peek(self): #does not remove
        return self.data[-1]
    
    def is_empty(self) -> bool:
        return len(self.data)==0
        # return not self.data
