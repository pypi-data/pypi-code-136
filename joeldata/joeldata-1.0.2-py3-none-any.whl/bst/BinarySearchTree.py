from TreeNode import TreeNode

'''
Best case: O(1) - find root
Worst Case: O(N) - full depth
Average Case: O(log₂N)
'''

class BST:
    root: (TreeNode | None) #can be empty or a node

    def __init__(self, root=None):
        self.root=root

    def __str__(self): #surrounded by half a box for clarity
        og_str=str(self.root)
        add_pipe=lambda s:'| '+s
        return '-----Binary Search Tree-----\n'+'\n'.join(map(add_pipe, og_str.split('\n')))
        
    def add(self, new_val): #iterative
        if self.root is None: #first time adding
            self.root=TreeNode(new_val)
            return
        
        node=self.root
        while True:
            if new_val<=node.get_data(): #go left
                if node.get_left():
                    node=node.get_left()
                else:
                    return node.set_left(TreeNode(new_val))
            else: #go right
                if node.get_right():
                    node=node.get_right()
                else:
                    return node.set_right(TreeNode(new_val))
    
    def add_recursively(self, new_val, node=None):
        node=node or self.root #default node is self.root

        if node is None: #exception
            self.root=TreeNode(new_val)
            return
        
        if new_val<=node.get_data(): #go left
            if node.get_left():
                return self.add_recursively(new_val, node.get_left())
            else:
                node.set_left(TreeNode(new_val))
                return
        elif new_val>node.get_data(): #go right
            if node.get_right():
                return self.add_recursively(new_val, node.get_right())
            else:
                node.set_right(TreeNode(new_val))
                return
    
    def search(self, target) -> bool:
        return self.search_for_nodes(target) is not None
    
    def search_for_node(self, target) -> TreeNode:
        return self.search_for_nodes(target)['current']
    
    def search_for_nodes(self, target) -> (None | dict[str, TreeNode]):
        curr=self.root
        parent=None
        relationship=None
        while curr: #keep going until curr does not exist
            if target==curr.get_data():
                return {
                    "current": curr,
                    "parent": parent,
                    "relationship": relationship #:('right'|'left') - current direction relative to parent 
                }
            elif target<curr.get_data():
                parent=curr
                curr=curr.get_left()
                relationship='left'
            elif target>curr.get_data():
                parent=curr
                curr=curr.get_right()
                relationship='right'
        return None

    def search_recursive(self, target, node=None) -> bool:
        node=node or self.root
        
        if node is None:
            return False
       
        if target<node.get_data():
            if node.get_left():
                return self.search_recursive(target, node.get_left())
            else:
                return False #no more nodes that could be value
        elif target>node.get_data():
            if node.get_right():
                return self.search_recursive(target, node.get_right())
            else:
                return False
        if target==node.get_data():
            return True
            
    def inorder(self, node=None):
        items=[]
        node=node or self.root
        if node.get_left(): #add left
            items+=self.inorder(node.get_left())
        items.append(node.get_data()) #add center
        if node.get_right(): #add right
            items+=self.inorder(node.get_right())
        return items

    def remove(self, target): # -> ('Target not present' | None):
        # 1. Get target
        to_del_nodes=self.search_for_nodes(target)
        to_del: TreeNode=to_del_nodes['current']

        # Case 1: Leaf
        if to_del.is_leaf(): #leaf does not use inline predecessor
            if to_del_nodes['relationship']=='left':
                to_del_nodes['parent'].set_left(None)
            elif to_del_nodes['relationship']=='right':
                to_del_nodes['parent'].set_right(None)
            else:
                raise Exception('Relationship', to_del_nodes['relationship'], 'is not "left" or "right"')
            return
        
        # 3.2 Find inorder predecessor & its parent
        curr=self.root #inorder predecessor
        curr_parent=self.root
        if self.root.get_left():
            curr=self.root.get_left()
        while curr.get_right():
            curr_parent=curr
            curr=curr.get_right()

        # Case 2: root
        if target==self.root.get_data():
            self.root.set_data(curr.get_data())
            if curr.get_left(): #do not miss curr's left
                curr_parent.set_right(curr.get_left()) # 4. Unlink curr & replace with curr's left
            else:
                curr_parent.set_right(None) #if no left to set, unlink curr from its parent 
            return
        
        # Case 3: inner node
        # 3.3 Replace to_del with inorder predecessor
        to_del.set_data(curr.get_data())
        #add curr's parent's right node to to_del's left
        if curr.get_left(): #do not miss curr's left
            curr_parent.set_right(curr.get_left()) # 4. Unlink curr & replace with curr's left
        else:
            curr_parent.set_right(None) #if no left to set, unlink curr from its parent


    def __contains__(self, target):
        return self.search(target)
    
    def __eq__(self, other):
        return str(self)==str(other) #str methods unambigously produce a string. If both strings are equal, trees are equal



BinarySearchTree=BST #alias
