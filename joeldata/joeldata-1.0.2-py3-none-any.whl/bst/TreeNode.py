class TreeNode:    
    def __init__(self, data, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

    def __str__(self, depth=0, side='root'):
        content=('> ' if depth==0 else '---> ')+side+' '+str(self.data)+'\n'
        if self.left:
            content+='\t'*depth+self.left.__str__(depth+1, 'left')
        if self.right:
            content+='\t'*depth+self.right.__str__(depth+1, 'right')
        return content
    
    def is_leaf(self) -> bool:
        return (not self.left) and (not self.right)
    
    def get_data(self):
        return self.data
    def set_data(self, new_data):
        self.data=new_data

    def get_left(self):
        return self.left
    def set_left(self, new_val):
        self.left=new_val
        return self #for piping

    def get_right(self):
        return self.right
    def set_right(self, new_val):
        self.right=new_val
        return self #for piping
    
    def __eq__(self, other):
        return self.get_data()==other.get_data()
    